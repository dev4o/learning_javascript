# not soloved - 77.273 points

wh_small_bottles = int(input())
wh_big_bottles = int(input())
truck_capacity = int(input())

big_bottles_liters = wh_big_bottles * 5

curr_capacity = truck_capacity - big_bottles_liters

small_bottles_total = 0

while curr_capacity > 0:
    if wh_small_bottles > 0:
        wh_small_bottles -= 1
        small_bottles_total += 1
        curr_capacity -= 1
    if wh_small_bottles == 0:
        break

if curr_capacity > 0:
    print("-1")
elif curr_capacity == 0:
    print(small_bottles_total)
elif small_bottles_total == 0 and curr_capacity == 0:
    print("-1")
