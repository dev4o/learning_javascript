kgarden = input()
n = int(input())

kgarden_number = int(''.join(filter(str.isdigit, kgarden)))

list1 = []
for _ in range(n):
    children = input()
    list1.append(children)


accepted = []
rejected = []
duplicate = []

for i in range(len(list1) - 1):
    current_number = list1[i]
    next_number = list1[i + 1]
    number1 = int(''.join(filter(str.isdigit, current_number)))
    number2 = int(''.join(filter(str.isdigit, next_number)))
    if number1 > number2:
        accepted.append(current_number)
    elif number1 < number2:
        rejected.append(next_number)

print(accepted)
print(rejected)
