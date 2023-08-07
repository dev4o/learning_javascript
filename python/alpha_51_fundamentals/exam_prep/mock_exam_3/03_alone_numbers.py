list1 = input().split(', ')
n = input()


# instead of pop and insert we can replace values using indexes
# ex: list1 = [1, 2, 3]
#     list1[0] = "2" = [2, 2, 3]

numbers_count = list1.count(n)

for i in range(numbers_count):
    numbers_index = list1.index(n)
    if (len(list1) - 1) == numbers_index:
        next_num = n
    else:
        next_num = list1[numbers_index + 1]

    if next_num > n:
        list1.pop(numbers_index)
        list1.insert(numbers_index, next_num)

str_to_int = [int(i) for i in list1]
print(str_to_int)

#
#Mock Exam 3 // Alone numbers

# tihomir kamenov - polovin reshenie
# da debugna, razbera i dovursha

# lst_numbers = input().split(', ')
# target = input()

# for i in range(1, len(lst_numbers) - 1):
#     if lst_numbers[i] == target:
#         if lst_numbers[i+1] != target and lst_numbers[i-1] != target:
#             if lst_numbers[i+1] > lst_numbers[i-1]:
#                 lst_numbers[i] = lst_numbers[i+1]