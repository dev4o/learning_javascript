deck = ['spades', 'clubs', 'hearts', 'diamonds']
card_n = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
list_letters = ['J', 'Q', 'K', 'A']

card = input()
if card.isdigit() and card in card_n:
    for x in range(2, int(card) + 1):
        for y in range(len(deck)):
            if y == len(deck) -1:
                print(f"{x} of {deck[y]}")
            else:
                print(f"{x} of {deck[y]}", end=', ')

elif not card.isdigit() and card in list_letters:
    index_card = list_letters.index(card)
    for x in range(index_card + 1):
        for y in range(len(deck)):
            if y == len(deck) -1:
                print(f"{list_letters[x]} of {deck[y]}")
            else:
                print(f"{list_letters[x]} of {deck[y]}",end=', ')
