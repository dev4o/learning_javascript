n = int(input())
list1 = []

for _ in range(n):
    num = int(input())
    list1.append(num)

counter = 1
max = 1

for i in range(len(list1) - 1):
    num1 = list1[i]
    num2 = list1[i + 1]
    if num1 == num2:
        counter += 1
    else:
        counter = 1
    if counter > max:
        max = counter

print(max)