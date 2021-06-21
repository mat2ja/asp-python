# Program to implement Hashing with Linear Probing
import random


class hashTable:
    # initialize hash Table
    def __init__(self):
        self.size = int(input("Upišite veličinu hash tabele : "))
        # initialize table with all elements 0
        self.table = [None for i in range(self.size)]
        self.elementCount = 0
        self.comparisons = 0

    # method that checks if the hash table is full or not
    def isFull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False

    # method that returns position for a given element
    def hashFunction(self, element):
        # return (element) % self.size
        p = 101
        a = random.randint(1, p-1)
        b = random.randint(0, p-1)
        return ((a*element + b) % p) % self.size

    # method that inserts element inside the hash table
    def insert(self, element):
        # checking if the table is full
        if self.isFull():
            print("Hash tabela je puna")
            return False

        isStored = False

        position = self.hashFunction(element)

        # checking if the position is empty
        if self.table[position] is None:
            self.table[position] = element
            print(f"Element {element} na poziciji {position}")
            isStored = True
            self.elementCount += 1

        # collision occured hence we do linear probing
        else:
            print(
                f"Dogodila se kolizija za element {element} na poziciji ... Traži se nova pozicija")

            while self.table[position] is not None:
                position += 1
                if position >= self.size:
                    position = 0

            self.table[position] = element
            isStored = True
            self.elementCount += 1
        return isStored

    # method that searches for an element in the table
    # returns position of element if found
    # else returns False

    def search(self, element):
        found = False

        position = self.hashFunction(element)
        self.comparisons += 1

        if self.table[position] == element:
            return position

        # if element is not found at position returned hash function
        # then first we search element from position+1 to end
        # if not found then we search element from position-1 to 0
        else:
            temp = position - 1
            # check if the element is stored between position+1 to size
            while position < self.size:
                if self.table[position] != element:
                    position += 1
                    self.comparisons += 1
                else:
                    return position

            # now checking if the element is stored between position-1 to 0
            position = temp
            while position >= 0:
                if self.table[position] != element:
                    position -= 1
                    self.comparisons += 1
                else:
                    return position

        if not found:
            print("Element not found")
            return False

    # method to remove an element from the table

    def remove(self, element):
        position = self.search(element)
        if position is not False:
            self.table[position] = None
            print(f"Element {element} je obrisan")
            self.elementCount -= 1
        else:
            print("Element nije prisutan u Hash tabeli")
        return

    # method to display the hash table

    def display(self):
        print()
        for i in range(self.size):
            print(f"{i} = {self.table[i]}")
        print(f"Broj elemenata u Hash tabeli je: {self.elementCount}")


# main function
table1 = hashTable()

# storing elements in table
table1.insert(12)
table1.insert(26)
table1.insert(31)
table1.insert(17)
table1.insert(90)
table1.insert(28)
table1.insert(88)
table1.insert(40)
table1.insert(77)       # element that causes collision at position 0

# displaying the Table
table1.display()
print()

# printing position of elements
print("The position of element 31 is : " + str(table1.search(31)))
print("The position of element 28 is : " + str(table1.search(28)))
print("The position of element 90 is : " + str(table1.search(90)))
print("The position of element 77 is : " + str(table1.search(77)))
print("The position of element 1 is : " + str(table1.search(1)))
print("\nTotal number of comparisons done for searching = " + str(table1.comparisons))
print()

table1.remove(90)
table1.remove(26)
elem = 88
print("Element:", elem,  "je nađen na poziciji: ",  table1.search(elem))
table1.display()
