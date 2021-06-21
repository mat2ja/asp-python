from stack_SLL import Stack


def reverse_string(string):
    S = Stack()
    reversed = ""
    for c in string:
        S.push(c)

    while not S.isEmpty():
        reversed += S.pop()

    return reversed


print(reverse_string("Matija"))
