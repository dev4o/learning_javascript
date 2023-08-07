vowels = 'aouei'
n = int(input())
ratio = 1
best = ""
max_vowels = 0
for _ in range(n):
    word = input()
 
    vowels_in_word = 0
    for l in word:
        if l in vowels:
            vowels_in_word += 1
    if vowels_in_word/len(word) < ratio:
        best = word
        max_vowels = vowels_in_word
        ratio = vowels_in_word/len(word)
    elif vowels_in_word/len(word) == ratio and vowels_in_word > max_vowels:
        best = word
        max_vowels = vowels_in_word
        ratio = vowels_in_word/len(word)
    elif vowels_in_word/len(word) == ratio and vowels_in_word == max_vowels and len(best) < len(word):
        best = word
        max_vowels = vowels_in_word
        ratio = vowels_in_word/len(word)
 
print(f"{best} {max_vowels}/{len(best)}")