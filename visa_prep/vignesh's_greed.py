n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
perimeter=-1
for i in range(n-2):
    if l[i]<l[i+1]+l[i+2]:
        perimeter=l[i]+l[i+1]+l[i+2]
        break
print(perimeter)
