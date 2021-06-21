# O(n)
def linearna_suma(A, n):
  """Vraća sumu prvih n brojeva u polju A"""
  if n == 0:
    return 0
  else:
    return linearna_suma(A, n-1) + A[n-1]


if __name__ == '__main__':
  A = [1, 2, 3, 4, 5, 7, 8, 9, 10, 34, 56, 9]
  rez = linearna_suma(A, 12)
  print(rez)
