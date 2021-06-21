
class Queue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            return "Queue empty!"

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        else:
            return "Queue empty!"
        """
        repr() compute the “official” string representation of an object (a representation 
        that has all information about the abject) and str() is used to 
        compute the “informal” string representation of an object 
        (a representation that is useful for printing the object).
        # example
        import datetime 
        today = datetime.datetime.now() 

        # Prints readable format for date-time object 
        print str(today) 

        # prints the official format of date-time object 
        print repr(today)   

        Output:

        2016-02-22 19:32:04.078030
        datetime.datetime(2016, 2, 22, 19, 32, 4, 78030)
        """

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return '{}'.format(self.out_stack)
        else:
            return "Queue empty!"

    def isEmpty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))


if __name__ == '__main__':
    queue = Queue()
    print("Is the queue empty? ", queue.isEmpty())
    print("Adding 0 to 10 in the queue...")
    for i in range(10):
        queue.enqueue(i)
    print("Queue size: ", queue.size())
    print("Queue peek : ", queue.peek())
    print("Dequeue...", queue.dequeue())
    print("Queue peek: ", queue.peek())
    print("Is the queue empty? ", queue.isEmpty())

    print("Printing the queue...")
    print(queue)
    print("Queue size: ", queue.size())