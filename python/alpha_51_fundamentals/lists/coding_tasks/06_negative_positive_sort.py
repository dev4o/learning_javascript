list_num = input().split(" ")

list_final = []
counter = 0

for i in list_num:
    if int(i) < 0:
        list_final.insert(counter, i)
        counter += 1
    else:
        list_final.append(i)
    
print(" ".join(list_final))
