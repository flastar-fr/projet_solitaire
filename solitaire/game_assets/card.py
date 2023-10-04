""" Card class """
dict_fam_log = {"Pique": "♠", "Coeur": "♥", "Carreau": "♦", "Trèfle": "♣"}


class Card:
    """ Queue class :
        :method get_attributs()
        :method get_value()
        :method get_family()
        :method get_visibility()
        :method set_visibility()

        :atr
    """
    def __init__(self, val, fam):
        self.value = val
        self.family = fam
        self.logo = dict_fam_log[fam]
        self.visibility = False

    # getters / setters
    def get_attributs(self) -> (str, str):
        """ Method to get card value and family

            :return (str, str): value and family
        """
        return self.value, self.logo

    def get_value(self) -> str:
        """ Method to get card value

            :return str: value
        """
        return self.value

    def get_family(self) -> str:
        """ Method to get card family

            :return str: family
        """
        return self.family

    def get_logo(self):
        """ Method to get card family

            :return str: logo
        """
        return self.logo

    def get_visibility(self) -> bool:
        """ Method to set card visibility

            :return bool: visibility
        """
        return self.visibility

    def set_visibility(self, val: bool):
        """ Method to set card visibily """
        self.visibility = val

    def __str__(self):
        return self.get_attributs()

    def __repr__(self):
        return str(self.get_attributs())
