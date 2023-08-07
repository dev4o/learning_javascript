import string
n = input()

temp_lower = ''
list1 = []
list2 = []

test_list = []

# 32 is ' ' (space)

for j in (n):
    if j in string.ascii_lowercase:
        temp_l = ord(j) - 97
        list1.append(temp_l)


n_2 = input()

for i in (n_2):
    if i in string.ascii_lowercase:
        temp_l2 = ord(i) - 97
        list2.append(temp_l2)


for each in range(len(list1)):
    counter = 0
    list1_v = list1[each]
    list2_v = list2[0] + counter
    test_list.append(list1_v - list2_v)
    counter += 1

# print(list1)
# print(list2)
print(test_list)