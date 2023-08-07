# Write a program that rotates a list several times (the first element becomes last).
# list = 1,2,3,4,5 and N = 2 -> result = 3,4,5,1,2

list1 = input().split(",")
rotation = int(input())

for _ in range(rotation):
    list1 = list1[1:] + [list1[0]]

print(",".join(list1))
