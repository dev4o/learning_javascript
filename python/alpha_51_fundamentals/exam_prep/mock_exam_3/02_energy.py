n = input()

list1 = []

energy = 0
coffee = 0

even = ''
odd = ''

result_even = 0
result_odd = 0

for i in n:
    list1.append(i)

for j in range(len(list1)):
    num_1 = list1[j]
    if int(num_1) % 2 == 0:
        energy += 1
        even += str(num_1)
    elif int(num_1) % 2 == 1:
        coffee += 1
        odd += str(num_1)

for a in even:
    result_even += int(a)

for b in odd:
    result_odd += int(b)

if result_even > result_odd:
    print(f"{result_even} energy drinks")
elif result_even < result_odd:
    print(f"{result_odd} cups of coffee")
else:
    print(f"{result_even} of both")