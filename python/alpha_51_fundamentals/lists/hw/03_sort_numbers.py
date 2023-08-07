# string to integer &&  integer to string in lists

num = input().split(", ")

str_to_int = [int(i) for i in num]
str_to_int.sort(reverse=True)

int_to_str = [str(i) for i in str_to_int]
print(", ".join(int_to_str))
