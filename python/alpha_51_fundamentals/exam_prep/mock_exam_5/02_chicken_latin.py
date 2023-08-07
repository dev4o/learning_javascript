# solved

in1 = input().split(" ")

vowel_low = "aeiou"
vowel_upp = "AEIOU"

list1 = []

test_slice = ''
suffix = 'che'


for i in in1:
    temp_word = i
    temp_letter = i[0]
    if temp_letter in vowel_low or temp_letter in vowel_upp:
        first_slice = temp_word[1:]
        second_slice = temp_word[0]
        if len(temp_word) % 2 == 0:
            suffix += 'e'
        test_slice += first_slice + second_slice + suffix
        list1.append(test_slice)
        suffix = 'che'
        test_slice = ''

    elif temp_letter not in vowel_low and temp_letter not in vowel_upp:
        if len(temp_word) % 2 == 0:
            suffix += 'e'
        temp_word = temp_word + suffix
        list1.append(temp_word)
        suffix = 'che'

print(" ".join(list1))
