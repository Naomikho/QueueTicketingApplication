from typing import List

"""Normally only one stack or queue is needed at a time unless a different kind of system"""
"""So singleton can be used on the Stack and Queue classes by using metaclass=Singleton under the class declaration"""

"""If array functions such as pop() are not used, one of the ways to remove an item from the stack or queue is array slicing.
   For example, for stack it would be Stack.stack[:Stack.size() - 1] to take everything but the last item, 
   and for queue it would be Queue.queue[1:] to take everything but the first item.
   Meanwhile, to replace len() we can create a class variable named counter to count the number of items in the stack/queue
   and increment/decrement the number as we enqueue and dequeue."""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class IQueuable:
   """This is a small program, so I will implement an informal interface
   that does not have strict enforcement."""

   def enqueue(value: str) -> List[str]:
       """adds value to the queue and returns new queue"""
       pass

   def dequeue() -> str:
       """removes item from queue, and returns the item removed"""
       pass
   
   def getQueue() -> List[str]:
       """returns a list of all the items in the queue"""
       pass
   
   def size() -> int:
       """returns the number of items in the queue"""
       pass

class Stack(IQueuable):
   """This class provides a stack implementation for IQueuable interface"""
   stack: List[str]

   def __init__(self):
       Stack.stack = []

   def enqueue(self, value: str) -> List[str]:
       """adds value to the queue and returns new queue"""
       Stack.stack.append(value)
       return Stack.stack

   def dequeue(self) -> str:
       """removes item from queue, and returns the item removed"""
       temp = Stack.stack[-1]
       Stack.stack.pop()
       return temp
   
   def getQueue(self) -> List[str]:
       """returns a list of all the items in the queue"""
       return Stack.stack
   
   def size(self) -> int:
       """returns the number of items in the queue"""
       return len(Stack.stack)

class Queue(IQueuable):
   """This class provides a queue implementation for IQueuable interface"""
   queue: List[str]

   def __init__(self):
       Queue.queue = []

   def enqueue(self, value: str) -> List[str]:
       """adds value to the queue and returns new queue"""
       Queue.queue.append(value)
       return Queue.queue

   def dequeue(self) -> str:
       """removes item from queue, and returns the item removed"""
       temp = Queue.queue[0]
       Queue.queue.pop(0)
       return temp
   
   def getQueue(self) -> List[str]:
       """returns a list of all the items in the queue"""
       return Queue.queue
   
   def size(self) -> int:
       """returns the number of items in the queue"""
       return len(Queue.queue)