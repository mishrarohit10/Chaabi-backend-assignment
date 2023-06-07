n = int(input("Enter number of elements : "))
lists = []
for i in range(0, n):
    ele = int(input())
    lists.append(ele)

idx1 = int(input("enter starting -> "))
idx2 = int(input("enter end index -> "))

# lists = [2,3,5,7,11,13,17,19,23,29,31,37,41] 
# idx1 = 2 , idx = 9
def f(lists, idx1, idx2):
    print(lists[idx1:idx2:2])

f(lists,idx1,idx2)
