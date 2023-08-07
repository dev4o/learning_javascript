kgarden = input()
n = int(input())

kgarden_number = int(''.join(filter(str.isdigit, kgarden)))
# points
# input orders wins

list1 = []
for _ in range(n):
    children = input()
    list1.append(children)

accepted = []
rejected = []
dupcliates = []

temp_n = int(''.join(filter(str.isdigit, list1[1])))
for i in list1[0:]:
    number1 = int(''.join(filter(str.isdigit, i)))
    if number1 > temp_n:
        temp_n = number1
        accepted.append(i)
    elif number1 == temp_n:
        dupcliates.append(i)
    else:
        rejected.append(i)


#first_of_duplicates = dupcliates[0]
#accepted.append(first_of_duplicates)

# dupcliates.pop(0)
# rejected.extend(dupcliates)

print(accepted)
print('---')
print(rejected)
print('----')
print(dupcliates)