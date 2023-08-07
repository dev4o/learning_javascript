# solved

n = int(input())

george_speed = int(input())
george_latency = int(input())

peter_speed = int(input())
peter_latency = int(input())

george_total = (n * george_speed) + 2 * george_latency
peter_total = (n * peter_speed) + 2 * peter_latency

if george_total < peter_total:
    print('George')
elif george_total > peter_total:
    print("Peter")
else:
    print("Draw")
