n = int(input())
yes_or_no = []
 
for i in range(n):
    numbers = input().split()
    for j in range(len(numbers)):
        if numbers[j] == numbers[len(numbers) - j - 1]:
            yes_or_no.append("Yes")
            break
        else:
            yes_or_no.append("No")
            break
 
for i in yes_or_no:
    print(i)