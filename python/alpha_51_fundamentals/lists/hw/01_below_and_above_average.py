numbers = input().split(",")

total_num = 0
below = []
above = []

for i in range(len(numbers)):
    nums = i + 1
    total_num += int(numbers[i])
    
total_num = f'{int(total_num) / int(nums):.2f}'
for i in range(len(numbers)):
    num = numbers[i]
    if int(num) < float(total_num):
        below.append(num)
    elif int(num) > float(total_num):
        above.append(num)

below_format = ",".join(below)
above_format = ",".join(above)

print(f"avg: {total_num}")
print(f"below: {below_format}")
print(f"above: {above_format}")