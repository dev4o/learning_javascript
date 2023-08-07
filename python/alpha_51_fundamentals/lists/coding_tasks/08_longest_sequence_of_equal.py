#algorithmic problem. possible for interview.

n = int(input())

list1 = []

for i in range(n):
    num = int(input())
    list1.append(num)

count = 1
max = 1

for i in range(len(list1) - 1):
    first_num = list1[i]
    second_num = list1[i + 1]
    if first_num == second_num:
        count += 1
    else:
        count = 1
    if count > max:
        max = count

print(max)