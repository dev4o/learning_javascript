n = int(input())

list1 = []

for _ in range(n):
    num = int(input())
    list1.append(num)

num = 0
counter = 0

for i in list1:
    count = list1.count(i)
    if count > counter:
        counter = count
        num = i

print(f"{num} ({counter} times)")