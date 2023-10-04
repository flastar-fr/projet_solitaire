""" Solitaire File manager """
# pylint: disable=E0401
import os
from json import load, dump
from game_assets.game_card import GameCard
from game_assets.stock_exception import StockException
from stack_n_queue.stack import Stack

families_list = ["Pique", "Coeur", "Carreau", "Trèfle"]
values_list = ["2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "V ", "D ", "R ", "As"]
dict_fam_color = {"Pique": "Noir", "Coeur": "Rouge", "Carreau": "Rouge", "Trèfle": "Noir"}


def generate_stock(game: GameCard) -> [Stack, Stack]:
    """ Function to generate the stock at the init of the game

        :arg game: game with cards (type: GameCard)
        :return: [Stack, Stack]: the complete stock
    """
    stock = Stack()
    for index in range(len(game)):
        stock.push(game.get_game()[index])

    return [Stack(), stock]


def generate_discard_pile(game) -> [Stack, Stack, Stack, Stack]:
    """ Function to generate the discard pile at the init of the game

        :arg game: game with cards (type: GameCard)
        :return: [Stack, Stack, Stack, Stack]: the complete discard pile
    """
    pile = [Stack(), Stack(), Stack(), Stack()]
    for index in range(4):
        for _ in range(index + 1):
            pile[index].push(game.get_a_card())
    for stack in pile:
        stack.get_top().set_visibility(True)

    return pile


def move_card(stack_to_push: Stack, stack_to_pop: Stack):
    """ Function to move a card between 2 game's stacks

        :param stack_to_push: game stack to push (type: Stack)
        :param stack_to_pop: game stack to pop (type: Stack)
    """
    stack_to_push.push(stack_to_pop.pop())


def move_verification(stack_to_push: Stack, stack_to_pop: Stack) -> bool:
    """ Function to verify if a move is possible

        :param stack_to_push: game stack to push (type: Stack)
        :param stack_to_pop: game stack to pop (type: Stack)

        :return bool: if the move is possible or not
    """
    if stack_to_push.is_empty() and stack_to_pop.get_top().get_value():
        return True

    couleur_push_to = dict_fam_color[stack_to_push.get_top().get_family()]
    couleur_pop_to = dict_fam_color[stack_to_pop.get_top().get_family()]
    index_push_to = values_list.index(stack_to_push.get_top().get_value())
    index_pop_to = values_list.index(stack_to_push.get_top().get_value())

    if couleur_push_to != couleur_pop_to and index_push_to == index_pop_to - 1:
        return True
    return False


def move_stock_to_found(stack_to_push: Stack, stack_to_pop: Stack) -> bool:
    """ Function to move a card between stock and foundation pile

        :param stack_to_push: game stack to push (type: Stack)
        :param stack_to_pop: game stack to pop (type: Stack)

        :return bool: if the move got realized or not
    """
    if move_verification(stack_to_push, stack_to_pop):
        move_card(stack_to_push, stack_to_pop)
        return True
    return False


def move_disc_to_found_n_reverse(stack_to_push, stack_to_pop, reverse: bool):
    """ Function to move a card between the discard pile and the foundation pile

        :param stack_to_push: game stack to push (type: Stack)
        :param stack_to_pop: game stack to pop (type: Stack)
        :param reverse: to know if we're where we move the card,
                        True : in foundation, False: in discard (type: bool)

        :return bool: if the move got realized or not
    """
    if reverse and move_verification(stack_to_pop, stack_to_push):
        move_card(stack_to_pop, stack_to_push)
        return True
    elif not reverse and move_verification(stack_to_push, stack_to_pop):
        move_card(stack_to_push, stack_to_pop)
        return True
    return False


def read_outputs() -> {}:
    """ Function to read the game outputs json file

        :return: {}: dict output
    """
    file_path = os.path.dirname(__file__)
    with open(os.path.join(file_path, "./game_output/outputs.json"),
              "r", encoding="utf-8") as file_reader:
        file = load(file_reader)
    return file


def write_outputs(outputs: {}):
    """ Function to write in the game outputs json file

        :arg outputs: dict to write
    """
    file_path = os.path.dirname(__file__)
    with open(os.path.join(file_path, "./game_output/outputs.json"), "w", encoding="utf-8") \
            as file_writer:
        dump(outputs, file_writer)


class Solitaire:
    """ Solitaire class:
        :method WIP

        :atr foundation_pile: foundation pile of the game (type: [Stack, Stack, Stack, Stack])
        :atr discard_pile: discard pile of the game (type:
        :atr stock:
    """
    def __init__(self, game_model):
        # game generation
        game = GameCard(game_model)
        game.shuffle_game()
        self.foundation_piles = [Stack(), Stack(), Stack(), Stack()]
        self.discard_pile = generate_discard_pile(game)
        self.stock = generate_stock(game)

        # others attributs
        self.outputs = read_outputs()
        self.stock_count = 0
        self.score = 0
        self.best_score = self.outputs["best_score"]

    def move_stock_to_trash(self, to_trash: bool):
        """ Method to move stock's cards in the trash

            :arg to_trash: to know if we're clearing the game trash or not,
                            True : in trash, False: out trash (type: bool)
        """
        if to_trash:
            move_card(self.stock[0], self.stock[1])
        else:
            move_card(self.stock[1], self.stock[0])

    def regenerate_stock(self):
        """ Method to regenerate the stock when it's empty """
        if not self.stock[1].is_empty():
            raise StockException("Stock is not empty !")
        for _ in range(len(self.stock[0])):
            self.move_stock_to_trash(False)
        self.stock_count += 1

    # getters / setters
    def get_foundation_piles(self) -> [Stack, Stack, Stack, Stack]:
        """ Method to get the foundation pile

            :return [Stack, Stack, Stack, Stack]: foundation pile
        """
        return self.foundation_piles

    def get_discard_pile(self) -> [Stack, Stack, Stack, Stack]:
        """ Method to get the discard pile

            :return [Stack, Stack, Stack, Stack]: discard pile
        """
        return self.discard_pile

    def get_stock(self) -> [Stack, Stack]:
        """ Method to get the game stock

            :return [Stack, Stack]: game stock
        """
        return self.stock

    def get_stock_count(self) -> int:
        """ Method to get the stock regeneration count

            :return int: stock regeneration count
        """
        return self.stock_count

    def get_score(self) -> int:
        """ Method to get the current score

            :return int: score
        """
        return self.score

    def get_best_score(self) -> int:
        """ Method to get the best score

            :return int: best score
        """
        return self.best_score
