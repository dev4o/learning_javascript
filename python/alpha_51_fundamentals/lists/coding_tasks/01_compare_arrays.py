n = int(input())

list1 = []
list2 = []

for i in range(n):
    list1.append(int(input()))

for i in range(n):
    list2.append(int(input()))

if list1 == list2:
    print('equal')
else:
    print('not equal')
