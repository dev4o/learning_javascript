# Write a program that finds all pairs of integers whose sum equals a given number.

n = int(input())
nums = input().split(" ")
str_to_int = [int(i) for i in nums]
list1 = []

is_pairs = False

for x in range(len(str_to_int)):
    for y in range(x + 1, len(str_to_int)):  
        if str_to_int[x] + str_to_int[y] == n:
            print(",".join(str(z) for z in [str_to_int[x], str_to_int[y]]))
            is_pairs = True

if not is_pairs:
    print('no pairs')