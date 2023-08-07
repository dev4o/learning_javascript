hidden_letter = 'h'

while True:
    your_letter = input()

    if hidden_letter == your_letter:
        print('You guessed correctly!')
        break
    elif hidden_letter > your_letter:
        print('My letter is bigger than your letter!')
    else:
        print("My letter is smaller than your letter!")
