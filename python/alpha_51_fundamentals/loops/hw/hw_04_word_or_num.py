in1 = input()
temp = ''
num1 = 0

for i in in1:
    temp += i


temp_num = ord(temp[0])
if 48 <= temp_num <= 57:
    if float(temp) % 1 == 0:
        num1 = int(temp) + 1
    elif float(temp) % 1 != 0:
        num1 = float(temp) + 1
elif temp_num == 45:
    num1 = int(temp) + 1
else:
    num1 = temp[::-1]

print(num1)
