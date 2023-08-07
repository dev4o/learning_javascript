in1 = int(input())

if 1 <= in1 <= 3:
    in1 *= 10
elif 4 <= in1 <= 6:
    in1 *= 100
elif 7 <= in1 <= 9:
    in1 *= 1000
else:
    in1 = 'invalid score'

print(in1)
