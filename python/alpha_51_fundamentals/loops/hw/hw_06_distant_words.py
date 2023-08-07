from string import ascii_letters
t = int(input())
n = int(input())

alpha = ascii_letters
counter = 0
total_sum = 0

for i in range(n):
    word = input()
    for chr in word:
        letters = len(word)
        if chr in alpha:
            counter += alpha.index(chr)
    sum = abs((counter + letters) - t)
    total_sum += sum
    print(word, sum) 
    counter = 0

print(f"{total_sum / n:.2f}")