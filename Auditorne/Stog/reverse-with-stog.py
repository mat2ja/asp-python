class Stack(object):
    def __init__(self):
        self.content = []
        self.min_array = []

    def push(self, value):

        self.content.append(value)

    def pop(self):
        if self.content:
            value = self.content.pop()

            return value
        else:
            return 'Empty List. '

    def size(self):
        return len(self.content)

    def isEmpty(self):
        return not bool(self.content)

    def peek(self):
        if self.content:
            return self.content[-1]
        else:
            print('Stack is empty.')

    def __repr__(self):
        return '{}'.format(self.content)


def reverse_string_with_stack(str1):

    s = Stack()
    revStr = ''

    for c in str1:
        s.push(c)

    while not s.isEmpty():
        revStr += s.pop()

    return revStr


if __name__ == '__main__':
    str1 = 'Ova jesen je kao produženo ljeto!'
    print(str1)
    print(reverse_string_with_stack(str1))
