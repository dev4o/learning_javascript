hy = int(input())

if hy <= 2:
    print(hy * 10)
else:
    remaining_years = hy - 2
    print((remaining_years * 4) + 20)