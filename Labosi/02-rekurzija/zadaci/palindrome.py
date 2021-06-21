def isPalindrome(izraz):
    if len(izraz) <= 2:
        return True
    elif izraz[0] != izraz[-1]:
        return False
    else:
        return isPalindrome(izraz[1:-1])


print(isPalindrome(''))
print(isPalindrome('k'))
print(isPalindrome('kk'))
print(isPalindrome('ada'))
print(isPalindrome('madam'))
print(isPalindrome('madom'))
print(isPalindrome('borat'))
print(isPalindrome("A Santa Lived As a Devil At NASA"))
