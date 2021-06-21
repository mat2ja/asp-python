# 2. Upotrebom mape napišite funkciju grupe koja grupira iste elemente u listu ili ntorku.

def grupe(arr):
    freq = {n: arr.count(n) for n in arr}

    output = []
    for k, v in freq.items():
        grupa = []
        for i in range(v):
            grupa.append(k)
        output.append(tuple(grupa))
    return output


print(grupe([1, 2, 1, 2, 3, 1, 1, 4]))
