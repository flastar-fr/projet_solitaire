from solitaire_game import Solitaire, move_card, move_verification


def show_game():
    stock = s.get_stock()
    foundation_piles = s.get_foundation_piles()
    discard_pile = s.get_discard_pile()
    # stock
    line_pattern = ["________", "|      |", "|      |", "|      |", "|      |", "--------"]
    if stock[1].is_empty():
        to_show_stock_n_found_pile = [" " * 11 for _ in line_pattern]
    else:
        to_show_stock_n_found_pile = ["\033[32m" + pattern + "\033[00m" for pattern in line_pattern]

    if not stock[0].is_empty():
        card = stock[0].get_top()
        color_code = "\033[30m" if card.get_family() in ["Pique", "Trèfle"] else "\033[31m"

        to_show_stock_n_found_pile[0] += f"{' ' * 3}{color_code}________\033[00m"
        to_show_stock_n_found_pile[1] += f"{' ' * 3}{color_code}|{card.get_logo()} " \
                                         f"{card.get_value()} {card.get_logo()}|\033[00m"
        to_show_stock_n_found_pile[2] += f"{' ' * 3}{color_code}|      |\033[00m"
        to_show_stock_n_found_pile[3] += f"{' ' * 3}{color_code}|      |\033[00m"
        to_show_stock_n_found_pile[4] += f"{' ' * 3}{color_code}|{card.get_logo()} " \
                                         f"{card.get_value()} {card.get_logo()}|\033[00m"
        to_show_stock_n_found_pile[5] += f"{' ' * 3}{color_code}--------\033[00m"
    else:
        card = ["   \033[90m" + pattern + "\033[00m" for pattern in line_pattern]
        to_show_stock_n_found_pile = \
            [line + line_card for line, line_card in zip(to_show_stock_n_found_pile, card)]

    # foundation pile
    for index in range(6):
        to_show_stock_n_found_pile[index] += "      "

    for index in range(4):
        if not foundation_piles[index].is_empty():
            card = foundation_piles[index].get_top()
            color_code = "\033[30m" if card.get_family() in ["Pique", "Trèfle"] else "\033[31m"

            to_show_stock_n_found_pile[0] += f"{' ' * 3}{color_code}________\033[00m"
            to_show_stock_n_found_pile[1] += f"{' ' * 3}{color_code}|{card.get_logo()} " \
                                             f"{card.get_value()} {card.get_logo()}|\033[00m"
            to_show_stock_n_found_pile[2] += f"{' ' * 3}{color_code}|      |\033[00m"
            to_show_stock_n_found_pile[3] += f"{' ' * 3}{color_code}|      |\033[00m"
            to_show_stock_n_found_pile[4] += f"{' ' * 3}{color_code}|{card.get_logo()} " \
                                             f"{card.get_value()} {card.get_logo()}|\033[00m"
            to_show_stock_n_found_pile[5] += f"{' ' * 3}{color_code}--------\033[00m"
        else:
            card = ["   \033[90m" + pattern + "\033[00m" for pattern in line_pattern]
            to_show_stock_n_found_pile = \
                [line + line_card for line, line_card in zip(to_show_stock_n_found_pile, card)]
            continue

    for index in to_show_stock_n_found_pile:
        print(index)

    print()

    # discard pile
    # discard_pile = [Stack, Stack, Stack] -> Stack lire uniquement, liste sans get element
    discard_pile_cards = []  # liste contenant les cartes
    for index in range(4):
        discard_pile_cards.append([])
        for element in discard_pile[index]:
            discard_pile_cards[index].append(element)

    # show hidden cards
    max_hidden_cards = max(len(discard_pile[0]), len(discard_pile[1]), len(discard_pile[2]),
                           len(discard_pile[3])) - 1  # nb max de ligne
    to_show_discard_hidden = ["   "] * (max_hidden_cards * 2)  # liste contenant les données

    # parcourir de 2 en 2 pour avoir le nombre max de ligne
    for index_get_cards_second, index_to_verify in enumerate(range(0, max_hidden_cards * 2, 2)):
        line = to_show_discard_hidden[index_to_verify]
        second_line = to_show_discard_hidden[index_to_verify + 1]
        for index_get_cards_first, stack in enumerate(discard_pile):
            # cas : carte définie sur visible, carte existente dans la stack
            if len(stack) - 1 > index_to_verify / 2 and \
                    discard_pile_cards[index_get_cards_first][index_get_cards_second].get_visibility():

                card = discard_pile_cards[index_get_cards_first][index_get_cards_second]
                color_code = "\033[30m" if card.get_family() in ["Pique", "Trèfle"] else "\033[31m"
                line += f"{color_code}|{card.get_logo()} " \
                        f"{card.get_value()} {card.get_logo()}|\033[00m"
                second_line += f"{color_code}________\033[00m"

            # cas : carte existente dans la stack
            elif len(stack) - 1 > index_to_verify / 2:
                line += "\033[32m|      |\033[00m   "
                second_line += "\033[32m________\033[00m   "

            # cas : carte n'existant pas dans la stack
            else:
                line += " " * 11
                second_line += " " * 11
        to_show_discard_hidden[index_to_verify] = line
        to_show_discard_hidden[index_to_verify + 1] = second_line

    for to_show in reversed(to_show_discard_hidden):
        print(to_show)

    # shown cards
    to_show_discard = ["", "", "", "", "", ""]
    for index in range(4):
        if not discard_pile[index].is_empty():
            card = discard_pile[index].get_top()
            color_code = "\033[30m" if card.get_family() in ["Pique", "Trèfle"] else "\033[31m"

            to_show_discard[0] += f"{' ' * 3}{color_code}________\033[00m"
            to_show_discard[1] += f"{' ' * 3}{color_code}|{card.get_logo()} " \
                                  f"{card.get_value()} {card.get_logo()}|\033[00m"
            to_show_discard[2] += f"{' ' * 3}{color_code}|      |\033[00m"
            to_show_discard[3] += f"{' ' * 3}{color_code}|      |\033[00m"
            to_show_discard[4] += f"{' ' * 3}{color_code}|{card.get_logo()} " \
                                  f"{card.get_value()} {card.get_logo()}|\033[00m"
            to_show_discard[5] += f"{' ' * 3}{color_code}--------\033[00m"
        else:
            to_show_discard = [line + " " * 11 for line in to_show_discard]
            continue

    for index in to_show_discard:
        print(index)


game_model = input("Please enter the number of card you want between 32 and 52 : ")
while game_model not in ["32", "52"]:
    game_model = input("Please select a valid number, 32 or 52 : ")

s = Solitaire(int(game_model))
s.move_stock_to_trash(True)
move_card(s.get_discard_pile()[3], s.get_discard_pile()[2])
show_game()

# print("t : retourner une carte du talon")
# print("d : effectuer un déplacement qui peut-être une défausse ou un rangement")
# print("x : abandonner la partie en cours")
# game_running = True
# while game_running:
#     user_answer = input("Veuillez choisir soit ")
