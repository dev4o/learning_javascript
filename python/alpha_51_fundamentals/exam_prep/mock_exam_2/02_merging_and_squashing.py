n = int(input())

result = ''
list1 = []
list2 = []
list3 = []
list4 = []

asd = ''

for i in range(n):
    num_1 = input()
    list1.append(num_1)

for j in range(n - 1):
    num_1 = list1[j]
    num_2 = list1[j + 1]
    list2.append(num_1[1] + num_2[0])
    list3.append(int(num_1[1]) + int(num_2[0])) # the b+c from // a(b+c)
    temp_n = int(list3[j])
    if temp_n < 10:
        temp_n = str(temp_n)
        list4.append(num_1[0] + str(temp_n) + num_2[1])
    else:
        temp_n = str(temp_n)
        list4.append(num_1[0] + str(temp_n[1]) + num_2[1])


print(" ".join(list2))
print(" ".join(list4))
