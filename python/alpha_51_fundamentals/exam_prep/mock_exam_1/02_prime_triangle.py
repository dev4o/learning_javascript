init_number = int(input())

list1 = [1]

for num in range(2, init_number + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) +1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        list1.append(num)

for prime in list1:
    for number in range(1, prime +1):
        if number in list1:
            print(1, end="")
        else:
            print(0, end="")
    print()