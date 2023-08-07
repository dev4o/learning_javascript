n = int(input())

list1 = []
result = []

for i in range(n):
    num = int(input())
    list1.append(num)


for x in range(len(list1)):
    for y in range(x + 1, len(list1)):
        if len(list1) == 1:
            result.append(num)
        elif len(list1) > 1 and list1[x] == list1[y]:
            result.append(list1[x])

if result:
    print(min(result))
else:
    print(list1[0])
