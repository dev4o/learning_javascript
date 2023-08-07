# for example:

n = int(input())

output = ''

for x in range(1, n + 1):
    output = output + str(x) + ' '
print(output)

# while exmple:

n = int(input())
x = 1
output=''

while x <= n:
    output = output + str(x) + ' '
    x = x + 1
print(output)