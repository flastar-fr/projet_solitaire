""" Queue class """
from typing import Any
from stack_n_queue_pop_exception import StackNQueuePopException


class Queue:
    """ Queue class :
        :method is_empty()
        :method get_first()
        :method push(data: Any)
        :method pop()
    """
    def __init__(self):
        self.queue = []

    def is_empty(self) -> bool:
        """ Method to verify if the queue is empty or not

            :return bool: answer of the question
        """
        return len(self.queue) == 0

    def get_first(self) -> Any:
        """ Method to get the queue's first element

            :return Any: first element of the queue
        """
        return self.queue[-1]

    def push(self, data: Any):
        """ Method to push in the queue

            :arg data: data to be push into the queue (type: Any)
        """
        self.queue.insert(0, data)

    def pop(self) -> Any:
        """ Method to pop in the queue

            :return Any: element that get remove
        """
        if self.is_empty():
            raise StackNQueuePopException("Pile is empty")
        return self.queue.pop()

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)
