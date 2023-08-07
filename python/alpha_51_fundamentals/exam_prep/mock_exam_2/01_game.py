n = input()

result = 0
list1 = []

for i in n:
    list1.append(int(i))

for i in range(1):
    sum_n = list1[0] + list1[1] + list1[2]
    product = list1[0] * list1[1] * list1[2]
    product_plus = list1[0] + list1[1] * list1[2]
    if product_plus > product:
        result = product_plus
    if sum_n > result:
        result = sum_n
    if product > product_plus:
       result = product


print(result)