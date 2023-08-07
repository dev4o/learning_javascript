# 500 ml = 0.1 deposit
# 1 liter = 0.25 deposit

half_liter_bottles = int(input())
liter_bottles = int(input())

print(f"{half_liter_bottles * 0.1 + liter_bottles * 0.25:.2f}")