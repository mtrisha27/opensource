n=int(input())
arr=list(map(int,input().split()))
a=arr[0]
for i in range(1,n):
    arr[i-1]=arr[i]
arr[n-1]=a
print(" ".join(map(str,arr)))
