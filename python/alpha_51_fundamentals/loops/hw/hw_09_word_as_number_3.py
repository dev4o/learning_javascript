n = int(input())
num = 0
text = ""
temp = input()
counter = n-1
while counter:
    line = input()
    counter -= 1
 
    if temp.replace("-", "").isnumeric() and line.replace("-", "").isnumeric():
        temp = str(int(temp) + int(line))
    elif temp.replace("-", "").isnumeric() and line.replace("-", "").isalpha():
        print(temp)
        temp = line
    elif temp.replace("-","").isalpha() and line.replace("-", "").isalpha():
        temp += "-" + line
    elif temp.replace("-","").isalpha() and line.replace("-", "").isnumeric():
        print(temp)
        temp = line
    elif not line.isalnum():
        print(temp)
        print(line)
        temp = input()
        counter -= 1
print(temp)