num = int(input())
prime_factors = []
 
for divisor in range(2, int(num ** 0.5) + 1):
    while num % divisor == 0:
        prime_factors.append(divisor)
        num //= divisor
 
if num != 1:
    prime_factors.append(num)
 
for factor in prime_factors:
    print(factor)