
# example 1:

i = 10
while i > 0:
    print(i)
    if i == 5:
        break
    i = i - 1

# example 2:

for i in range(1, 10):
    print(i)
    if i == 5:
        break

# continue example:

for n in range(0, 10):
    if n % 2 == 1:
        continue
    print(n)