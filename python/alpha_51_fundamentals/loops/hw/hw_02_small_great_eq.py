n = int(input())

temp_n = ''
sum = ''

for i in range(n):
    number = int(input())

    if i == 0:
        sum = str(number)
    elif i >= 1:
        if int(temp_n) > int(number):
            sum += ('>' + str(number))
        elif int(temp_n) < int(number):
            sum += ('<' + str(number))
        elif int(temp_n) == int(number):
            sum += ('=' + str(number))

    temp_n = str(number)

print(sum)
