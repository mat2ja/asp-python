# 3. Napišite funkciju dubina_bsp koja vraća dubinu zadanog binarnog stabla. Na primjer, ako
# se korijen stabla nalazi na dubini 0 onda


def dubina_bsp(arr, dubina=-1):
    if not isinstance(arr, list) or arr is None or len(arr) == 0:
        return dubina

    # root, left, right = arr[0],arr[1],arr[2]
    root, left, right = arr

    if root:
        dubina += 1
        dubinaL = dubina_bsp(left, dubina)
        dubinaR = dubina_bsp(right, dubina)
        dubina = max(dubinaL, dubinaR)

    return dubina


def dubina_bsp(lista, d=0):
    if not isinstance(lista, list) or len(lista) < 1:
        return d
    x = dubina_bsp(lista[1], d + 1)
    y = dubina_bsp(lista[2], d + 1)
    if x > y:
        return x
    return y


l = dubina_bsp([17, [8, None, [12, 9, None]], [31, 20, [45, 32, 56]]])
l1 = dubina_bsp([])
l2 = dubina_bsp([17, None, None])

print(f"Dubina je {l}")
print(f"Dubina je {l1}")
print(f"Dubina je {l2}")
