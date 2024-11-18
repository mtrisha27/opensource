n=int(input())
i=int(input())
if n & (1<<(i-1)):
    print("true")
else:
    print("false")
