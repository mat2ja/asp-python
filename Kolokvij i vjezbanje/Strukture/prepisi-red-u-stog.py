from queue_DLL import LinkedQueue
from stack_SLL import Stack


def queueToStack(red):
    stog = Stack()
    while not red.isEmpty():
        removed = red.dequeue()
        stog.push(removed)
    return stog


def queueToStackNth(red, k):
    stog = Stack()
    n = 1
    while not red.isEmpty():
        removed = red.dequeue()
        if n == k:
            stog.push(removed)
            n = 1
        else:
            n += 1
    return stog


Q = LinkedQueue()
for i in range(1, 5):
    Q.enqueue(i)
Q.printQueue()
S = queueToStack(Q)
S.printStack()

Q2 = LinkedQueue()
for i in range(1, 5):
    Q2.enqueue(i)
Q2.printQueue()
S2 = queueToStackNth(Q2, 2)
S2.printStack()

'''
Printing queue: 1 2 3 4 
4 3 2 1
Printing queue: 1 2 3 4
4 2
'''
