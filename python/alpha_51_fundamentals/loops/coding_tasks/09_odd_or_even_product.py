in1 = int(input())
in2 = input()

counter = 1
even_n = 1
odd_n = 1

for num in in2:
    if num.isdigit():
        if counter % 2 == 0:
            even_n *= int(num)
        elif counter % 2 != 0:
            odd_n *= int(num)
        counter += 1


if even_n == odd_n:
    print(f"yes {even_n}")
else:
    print(f"no {odd_n} {even_n}")