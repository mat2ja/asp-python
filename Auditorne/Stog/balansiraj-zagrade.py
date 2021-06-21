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


def balance_par_str_with_stack(str1):

    s = Stack()
    balanced = True
    index = 0

    while index < len(str1) and balanced:

        symbol = str1[index]

        if symbol == "(":
            s.push(symbol)

        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True

    else:
        return False


if __name__ == '__main__':
    print(balance_par_str_with_stack('(((())))'))
    print(balance_par_str_with_stack('((((())'))
    print(balance_par_str_with_stack('((((())))'))
