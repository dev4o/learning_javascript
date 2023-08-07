kgarden = input()
n = int(input())

kgarden_number = int(''.join(filter(str.isdigit, kgarden)))

list1 = []
for _ in range(n):
    children = input()
    list1.append(children)

largest_objects = []
for obj in list1:
    num_value = int(obj[-2:])  # Extract the numerical value from the string
    if len(largest_objects) < 4:
        largest_objects.append(obj)
    else:
        min_value = int(largest_objects[0][-2:])
        min_index = 0
        for i in range(1, 4):
            current_value = int(largest_objects[i][-2:])
            if current_value < min_value:
                min_value = current_value
                min_index = i
        if num_value > min_value:
            largest_objects[min_index] = obj

for obj in largest_objects:
    print(obj)