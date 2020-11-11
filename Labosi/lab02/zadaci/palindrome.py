def isPalindrome(izraz):
    if len(izraz) <= 1 or izraz[0] != izraz[-1]:
        return False
    elif len(izraz) <= 3:
        return izraz[0] == izraz[-1]
    else:
        return isPalindrome(izraz[1:-1])


print(isPalindrome(''))
print(isPalindrome('k'))
print(isPalindrome('kk'))
print(isPalindrome('ada'))
print(isPalindrome('madam'))
print(isPalindrome('borat'))
