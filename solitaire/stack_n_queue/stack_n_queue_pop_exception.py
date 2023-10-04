""" Exception for Stacks and Queues pop method """


class StackNQueuePopException(Exception):
    """ Raise when the stack or the queue is empty """
    def __init__(self, message="An error occured"):
        self.message = message
        super().__init__(self.message)
