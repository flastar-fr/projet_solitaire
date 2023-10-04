""" Stack class """
from typing import Any
from .stack_n_queue_pop_exception import StackNQueuePopException


class Stack:
    """ Stack class :
        :method is_empty()
        :method get_top()
        :method push(data: Any)
        :method pop()

        :atr
    """
    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        """ Method to verify if the stack is empty or not
        
            :return bool: answer of the question
        """
        return len(self.stack) == 0

    def get_top(self) -> Any:
        """ Method to get the stack's top
        
            :return Any: top of the stack
        """
        if self.is_empty():
            raise StackNQueuePopException("Stack is empty !")
        return self.stack[-1]

    def push(self, data: Any):
        """ Method to push in the stack

            :arg data: data to be push into the stack (type: Any)
        """
        self.stack.append(data)

    def pop(self) -> Any:
        """ Method to pop in the stack
        
            :return Any: element that get remove
        """
        if self.is_empty():
            raise StackNQueuePopException("Stack is empty")
        return self.stack.pop()

    def __iter__(self):
        for data in self.stack:
            yield data

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return "| " + str(self.stack)[1:-1] + " |"

    def __repr__(self):
        return "| " + str(self.stack)[1:-1] + " |"
