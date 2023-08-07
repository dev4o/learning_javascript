command = input()

x = 0
y = 0

for i in command:
    if i == "U":
        y += 1
    elif i == "D":
        y -= 1
    elif i == "L":
        x -= 1
    elif i == "R":
        x += 1

print((x, y))