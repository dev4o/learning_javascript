n = int(input())

total_sum = 0
list1 = []

for i in range(n):
    nums = float(input())
    total_sum += nums
    if -10000 <= float(nums) and float(nums) <= 10000:
        list1.append(nums)

print(f"min={min(list1):.2f}")
print(f"max={max(list1):.2f}")
print(f"sum={total_sum:.2f}")
print(f"avg={total_sum / n:.2f}")