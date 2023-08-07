# Constraints
# 1 <= HY <= 15
# Input
# 2
# Output
# 20

hy = int(input())

if hy <= 2:
    print(hy * 10)
else:
    remaining_years = hy - 2
    print((remaining_years * 4) + 20)
