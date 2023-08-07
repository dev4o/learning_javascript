in1 = float(input())
in2 = float(input())
in3 = float(input())

sum = in1 * in2 * in3

if sum < 0:
    print('-')
if sum > 0:
    print('+')
if sum == 0:
    print(0)