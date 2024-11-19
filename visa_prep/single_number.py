n=int(input())
a=list(map(int,input().split()))
unique_num=0
for num in a:
    unique_num^=num
print(unique_num)
