a = float(input())
b = float(input())

if a > b:
    if a % 1 == 0 and b % 1 == 0: # if both are integers
        print(int(b), int(a))
    else:
        print(b, a)

else:
    if a % 1 == 0 and b % 1 == 0: # if both are integers
        print(int(a), int(b))
    else:
        print(a, b)    