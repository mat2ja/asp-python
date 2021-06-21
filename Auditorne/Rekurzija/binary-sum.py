import random


def binary_sum(S, start, stop):
  """Vraća sumu brojeva u implicitnom nizu S[start:stop]."""
  
  if start >= stop:                      # 0 elemenata u nizu - osnovni slučaj
    return 0
  elif start == stop-1:                  # 1 element u nizu - osnovni slučaj
    return S[start]
  else:                                  # dva ili više elemenata u nizu - rekurzivni poziv dok se ne dosegne osnovni slučaj
    mid = (start + stop) // 2
    return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


if __name__ == '__main__':
  S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  S1 = []
  for i in range(100):
      S1.append(random.randint(1, 200))
  S1.sort()
  a = binary_sum(S, 0, 10)
  b = binary_sum(S1, 0, len(S1))
  print(a)
  print(b)
