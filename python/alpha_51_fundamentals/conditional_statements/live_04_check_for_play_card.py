in1 = input()

if in1.isdigit() and 2 <= int(in1) <=10:
    print('yes')
elif in1 == 'A' or in1 == 'K' or in1 == 'Q' or in1 == 'J':
    print('yes')
else:
    print('no')