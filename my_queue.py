"""
from collections import deque

q = deque()
q += [1, 3, 4]
q.popleft()
"""

class Queue:
    def __init__(self):
        self.array = list()

    def enqueue(self, val):
        """Put item at the back
        """
        self.array.append(val)

    def dequeue(self):
        """Get item at the front
        """
        if len(self.array) == 0:
            return None

        return self.array.pop(0)


q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(2)
q.dequeue()
print(q.array)