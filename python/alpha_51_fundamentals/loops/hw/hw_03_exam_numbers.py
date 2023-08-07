x = int(input())
y = int(input())
t = int(input())

for i in range(x, y + 1):
    temp_n = str(i)
    n1 = temp_n[0]
    n2 = temp_n[1]
    n3 = temp_n[2]
    total = int(n1) + int(n2) + int(n3)
    if total == t:
        print(temp_n)
