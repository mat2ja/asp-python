from stack_SLL import Stack


def is_paren_balanced(string):
    S = Stack()
    for p in string:
        if p in "({[":
            S.push(p)
        else:
            if S.isEmpty():
                return False
            else:
                popped = S.pop()
                if p == "(" and popped != ")"  \
                        or p == "[" and popped != "]"  \
                        or p == "{" and popped != "}":
                    return False

    return True


print(is_paren_balanced("(((({}))))"))

print(is_paren_balanced("[][]]]"))
print(is_paren_balanced("[][]"))
