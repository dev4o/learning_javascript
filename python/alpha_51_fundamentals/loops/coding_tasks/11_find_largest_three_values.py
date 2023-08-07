n = int(input())

list1 = []

for i in range(n):
    num = int(input())
    list1.append(num)

list1.sort()
print(f"{list1[-1]}, {list1[-2]} and {list1[-3]}")
