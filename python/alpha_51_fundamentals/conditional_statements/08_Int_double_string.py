in1 = input()
variable = input()

if in1 == 'integer':
    result = int(variable)
    print(result + 1)
elif in1 == 'real':
    result = float(variable)
    print(f'{result + 1:.2f}')
elif in1 == 'text':
    print(f"{variable}*")