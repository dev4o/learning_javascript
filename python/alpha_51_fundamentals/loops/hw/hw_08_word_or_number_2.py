n = int(input())

digits_total = 0
list2 = []

for i in range(n):
    input_1 = input()
    if input_1.isdigit():
        digits_total += int(input_1)
    elif not input_1.isdigit():
        list2.append(input_1)


if not list2:
    print('no words')
elif list2:
    sep = "-"
    x = sep.join(list2)
    print(x)

print(digits_total)
