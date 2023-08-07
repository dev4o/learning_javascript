# solved
#alphabet letter to number
import string
n = int(input())

best_word = ''
best_score = 0

for i in range(n):
   word = input()
   temp_final = 0
   for j in word:
    temp_lower = 0
    temp_upper = 0
    if j in string.ascii_lowercase:
      temp_lower += (ord(j) - 96)

    elif j in string.ascii_uppercase:
      temp_upper += (ord(j) - 64)

    temp_final += temp_lower + temp_upper
    if best_score < temp_final:
      best_score = temp_final
      best_word = word

print(best_score, best_word, end=' ')
