# solved

list1 = []
temp_list = []

for _ in range(5):
    nums = input()
    list1.append(nums)

for x in range(len(list1)):
    num_1 = list1[x]
    test = int(num_1[0]) * int(num_1[1]) * int(num_1[2])
    if 99 > int(test) > 9:
        test = str(test)
        temp_list.append(test[1])
    elif int(test) > 99:
        test = str(test)
        temp_list.append(test[2])
    elif int(test) < 10:
        test = str(test)
        temp_list.append(test[0])

print("".join(temp_list))