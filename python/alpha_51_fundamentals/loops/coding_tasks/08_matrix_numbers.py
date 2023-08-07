number = int(input())
for i in range(1, number + 1):
    for b in range(1, number + 1):
        print(i + b - 1, end=' ')
    print()