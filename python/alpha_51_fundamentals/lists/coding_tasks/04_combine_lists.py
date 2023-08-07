list1 = input().split(",")
list2 = input().split(",")

final_list = []

for i in list1:
    final_list.append(i)

counter = 1
for i in list2:
    final_list.insert(counter,i)
    counter += 2

print(",".join(final_list))
