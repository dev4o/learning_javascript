n = int(input())

max_num = -201

for _ in range(n):
    temp_num = int(input())
    if max_num < temp_num:
        max_num = temp_num

print(max_num)