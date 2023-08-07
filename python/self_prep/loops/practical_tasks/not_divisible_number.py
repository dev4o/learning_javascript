n = int(input())

temp_v = ''

# Output should always consists of the numbers 
# from 1 to N, which are not divisible by 3 or 7, 
# separated by a whitespace.


for i in range(1, n + 1):
    temp_e = i / 3
    temp_b = i / 7
# if temps are not integers when divided, add to temp_v
# if they are integers, do nothing
    if temp_e % 1:
        if temp_b % 1:
# one line alternative:
# if i % 3 == 0 or i %  7 == 0:
            temp_v += str(i) + ' '
# alternative 1 line print without the need of "temp_v":
# print(i, end=' ')
print(temp_v)
