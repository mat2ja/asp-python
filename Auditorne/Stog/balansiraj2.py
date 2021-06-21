def isBalanced(str):
    s = []
    is_balanced = True
    i = 0
    while i < len(str) and is_balanced:
        paren = str[i]
        if paren == "(":
            s.append(paren)
        elif paren == ")":
            if s:
                s.pop()
            else:
                is_balanced = False
        i += 1
    if s:
        is_balanced = False
    return is_balanced


if __name__ == '__main__':
    print(isBalanced('(())'))
    print(isBalanced('((((())'))
