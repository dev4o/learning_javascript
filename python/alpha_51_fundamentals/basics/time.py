d = int(input())
h = int(input())
m = int(input())
s = int(input())

d *= 24 * 60 * 60
h *= 60 * 60
m *= 60

print(d + h + m + s)