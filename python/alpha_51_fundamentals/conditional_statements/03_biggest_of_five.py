in1 = int(input())
in2 = int(input())
in3 = int(input())
in4 = int(input())
in5 = int(input())

big_num = 0

if in1 >= in2 and in1 >= in3 and in1 >= in4 and in1 >= in5:
    big_num = in1
if in2 >= in1 and in2 >= in3 and in2 >= in4 and in2 >= in5:
    big_num = in2
if in3 >= in1 and in3 >= in2 and in3 >= in4 and in3 >= in5:
    big_num = in3
if in4 >= in1 and in4 >= in2 and in4 >= in3 and in4 >= in5:
    big_num = in4
if in5 >= in1 and in5 >= in2 and in5 >= in3 and in5 >= in4:
    big_num = in5

print(big_num)