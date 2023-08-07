n = int(input())

temp_n = 1
result = 0
asd = 0


for i in range(n):
    if n > temp_n:
        result += 1
    temp_n += 2
    if n >= 10:
        result -= 1
  

print(result - asd)