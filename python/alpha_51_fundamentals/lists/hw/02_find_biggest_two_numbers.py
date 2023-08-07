num = input().split(" ")

test = [int(i) for i in num]
test.sort()
print(test[-1], test[-2])
