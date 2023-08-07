n = int(input())
 
for _ in range(n):
    x = "true"
    line = input().split(",")
    first = int(line[0])
    for i in range(1, len(line)):
        if int(line[i]) < int(line[i-1]):
            x = "false"
 
    print(x)