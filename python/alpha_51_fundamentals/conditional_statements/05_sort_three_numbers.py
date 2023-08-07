in1 = int(input())
in2 = int(input())
in3 = int(input())

big_n = 0
mid_n = 0
smol_n = 0

if in1 >= in2 and in1 >= in3:
    big_n = in1
    if in2 > in3:
        mid_n = in2
        smol_n = in3
    else:
        mid_n = in3
        smol_n = in2
if in2 >= in1 and in2 >= in3:
    big_n = in2
    if in1 > in3:
        mid_n = in1
        smol_n = in3
    else:
        mid_n = in3
        smol_n = in1
if in3 >= in1 and in3 >= in2:
    big_n = in3
    if in1 > in2:
        mid_n = in1
        smol_n = in2
    else:
        mid_n = in2
        smol_n = in1

print(f'{big_n} {mid_n} {smol_n}')