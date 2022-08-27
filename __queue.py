from typing import List

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