

''' Koristimo stog za okretanje stringa '''

from linked_stack import Stack

def okreni_string_sa_stog(str1):

  s = Stack()
  revStr = ''

  for c in str1:
    s.push(c)

  while not s.isEmpty():
    revStr += s.pop()

  return revStr



if __name__ == '__main__':
  str1 = 'Jesen stize dunjo moja'
  print(str1)
  print(okreni_string_sa_stog(str1))



