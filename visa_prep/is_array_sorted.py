n=int(input())
arr=list(map(int,input().split()))
flag=True
for i in range(1,n):
    if arr[i]<arr[i-1]:
        flag=False
        break
if flag:
    print("true")
else:
    print("false")
