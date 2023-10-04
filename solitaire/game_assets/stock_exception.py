""" Exception for stock """


class StockException(Exception):
    """ Raise when the stock is empty """
    def __init__(self, message="An error occured"):
        self.message = message
        super().__init__(self.message)
