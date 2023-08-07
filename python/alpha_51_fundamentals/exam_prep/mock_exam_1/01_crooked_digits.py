# Sums the digits of the number N and stores the result back in N
# If the obtained result is bigger than 9, step 1. is repeated
# otherwise the algorithm finishes


input_number = input().replace("-","").replace(".","")

while len(input_number) > 1:
    curr_num = 0

    for char in input_number:
        curr_num += int(char)
    
    input_number = str(curr_num)

print(input_number)
