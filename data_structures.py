# Data Primitives:
from typing import List


some_bool = True
some_int = 0
some_float = 0.0

# Data Structure (Sort Of)
fib = [
    1, 1, 2, 3, 5, 8,
    13, 21, 34, 55, 89
]

class Queue:
    """
    This is a FIFO data structure, otherwise known as a Queue.
    e.g.:
        FIFO.enqueue(1) --> [1]
        FIFO.enqueue(2) --> [1, 2]
        FIFO.dequeue() --> [2] returns 1
        FIFO.dequeue() --> [] returns 2
    """
    _items: List

    def __init__(self) -> None:
        self._items = []

    def __repr__(self) -> str:
        return f"<Queue len={len(self._items)}>"
    
    def __bool__(self) -> bool:
        return bool(len(self._items))

    def enqueue(self, item) -> None:
        self._items.append(item)

    def dequeue(self):
        if len(self._items):
            return self._items.pop(0)
        return None


checkout_01 = Queue()
checkout_02 = Queue()

for i in range(33):
    if not i % 3:
        checkout_01.enqueue(i)
    else:
        checkout_02.enqueue(i)

print("01", checkout_01)
print("02", checkout_02)

while (checkout_01 or checkout_02):
    print("01", checkout_01.dequeue(), end=", ")
    print("02", checkout_02.dequeue())

print("01", checkout_01)
print("02", checkout_02)
