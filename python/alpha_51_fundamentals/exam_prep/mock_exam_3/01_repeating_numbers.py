n = int(input())

list1 = []

for i in range(n):
    num = int(input())
    list1.append(num)

print(max(set(list1), key=list1.count))