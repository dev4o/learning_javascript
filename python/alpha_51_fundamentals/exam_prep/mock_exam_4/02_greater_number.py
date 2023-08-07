list1 = [int(i) for i in input().split(",")]
list2 = [int(i) for i in input().split(",")]

result = []

for first_num in list1:
    index_first_num = list2.index(first_num)
    next_greater_num = -1

    for second_num in list2[index_first_num + 1:]:
        if second_num > first_num:
            next_greater_num = second_num
            break
    
    result.append(next_greater_num)

print(",".join(str(x) for x in result))
