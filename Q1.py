def selectionSort(list,size):
    for i in range(size):
        min_idx = i

        for j in range(i + 1, size):
            if list[j] < list[min_idx]:
                min_idx = j

        (list[i], list[min_idx]) = (list[min_idx],list[i])

list = []
n = int(input("Enter number of elements -> "))

for i in range(0,n):
    element = int(input())
    list.append(element)

size = len(list)
selectionSort(list,size)

print(list)

