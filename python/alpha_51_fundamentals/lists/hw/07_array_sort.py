num = input().split(",")

counter = 0
for i in range(len(num)):
    if num[i] == '0':
        counter += 1

for i in range(counter):
    num.remove('0')

for i in range(counter):
    num.append('0')  

print(",".join(num))