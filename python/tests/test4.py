#Mock Exam 3 // Alone numbers

# tihomir kamenov - polovin reshenie
# da debugna, razbera i dovursha

lst_numbers = input().split(', ')
target = input()

for i in range(1, len(lst_numbers) - 1):
    if lst_numbers[i] == target:
        if lst_numbers[i+1] != target and lst_numbers[i-1] != target:
            if lst_numbers[i+1] > lst_numbers[i-1]:
                lst_numbers[i] = lst_numbers[i+1]