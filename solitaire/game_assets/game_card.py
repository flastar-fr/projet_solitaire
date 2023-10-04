""" class GameCard """

from random import choice, shuffle
from .card import Card

families_list = ["Pique", "Coeur", "Carreau", "Trèfle"]
values_list = ["2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "V ", "D ", "R ", "As"]


class GameCard:
    """ Stack class :
        :method get_model()
        :method get_game()
        :method set_model(model: int)
        :method get_a_card()
        :method shuffle_game()

        :atr model: the number of cards (32 or 52)
    """
    def __init__(self, model):
        self.model = model
        if model == 32:
            self.game = [Card(v, f) for v in values_list[5:] for f in families_list]
        else:
            self.game = [Card(v, f) for v in values_list for f in families_list]

    def get_model(self) -> int:
        """ Method to get game model

            :return int: game model
        """
        return self.model

    def get_game(self) -> [Card]:
        """ Method to get list of cards

            :return [Card]: card list
        """
        return [c for c in self.game]

    def set_model(self, model: int):
        """ Method to get card value and family

            :param model: set a new game model, 32 or 52 (type: int)
        """
        self.game = GameCard(model)

    def get_a_card(self) -> (str, str):
        """ Method to randomly chose a card in the game

            :return (str, str): value and family
        """
        card = choice(self.game)
        self.game.remove(card)
        return card

    def shuffle_game(self):
        """ Method to shuffle the game """
        shuffle(self.game)

    def __str__(self):
        return str(self.game)

    def __len__(self):
        return len(self.game)
