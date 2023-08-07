import sys

n = int(input())

list1 = []
max_sum = -sys.maxsize

if 1 <= n <= 1024:
    for i in range(n):
        num = int(input())
        list1.append(num)
else:
    exit()

temp_sum = list1[0]
for x in range(len(list1) - 1):
    second_num = list1[x + 1]
    if temp_sum >= 0:
        temp_sum += second_num
    else:
        temp_sum = 0

    if max_sum < temp_sum:
        max_sum = temp_sum


print(max_sum)
