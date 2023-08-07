n = int(input())

sum = 0

for i in range(n):
    num = float(input())
    sum += num / n

print(f'{sum:.2f}')