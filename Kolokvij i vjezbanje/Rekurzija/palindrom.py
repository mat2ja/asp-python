# 3. Napišite rekurzivnu funkciju palindrom koja vraća True ako je zadani string palindrom
# (isti s lijeva i zdesna), u suprotnom vraća False.

def palindrom(S):
    S = S.strip().replace(" ", "").lower()
    if len(S) <= 2:
        return True
    elif S[0] != S[-1]:
        return False
    else:
        return palindrom(S[1:-1])


# def palindrom(S):
#     S = S.strip().replace(" ", "").lower()
#     return S == S[::-1]


print(palindrom(''))
print(palindrom('k'))
print(palindrom('kk'))
print(palindrom('ada'))
print(palindrom('madam'))
print(palindrom('madom'))
print(palindrom('borat'))
print(palindrom("A Santa Lived As a Devil At NASA"))
