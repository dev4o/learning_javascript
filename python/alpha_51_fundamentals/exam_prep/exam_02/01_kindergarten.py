kgarden = input()
n = int(input())

kgarden_number = int(''.join(filter(str.isdigit, kgarden)))
# points
# input orders wins

list1 = []
for _ in range(n):
    children = input()
    list1.append(children)

#print(list1)

temp_list = []
accepted_list = []
rejected_list = []

temp_n = 0
big_n = 0
last = list1[-1]
for i in range(len(list1) - 1):
    score = list1[i]
    score2 = list1[i + 1]
    number1 = int(''.join(filter(str.isdigit, score)))
    number2 = int(''.join(filter(str.isdigit, score2)))
    if number1 > number2:
        big_n = number1
        if score not in temp_list:
            temp_list.append(score)
    elif big_n < number2:
        big_n = number2
        temp_list.append(score2)
    else:
        rejected_list.append(score)

print(temp_list)
print(rejected_list)
