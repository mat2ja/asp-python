# Python program za implementaciju
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Srednji član polja koje se sortira
        L = arr[:mid]  # Podjela elemenata polja na dvije polovine
        R = arr[mid:]

        mergeSort(L)  # Sortiranje prve polovine
        mergeSort(R)  # Sortiranje druge polovine
        # incijalizacija merge operacije
        i = j = k = 0

        # kopirnje podataka sa temporari polja L[] i R[]
        # operacija merge
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
arr = [12, 11, 13, 5, 6, 7]
print("\nTest primjer - zadano polje je: ", end="\n")
printList(arr)
mergeSort(arr)
print("\nTest primjer -Ssortirano polje je  ", end="\n")
printList(arr)
