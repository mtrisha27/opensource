n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
rsum=[0]*n
csum=[0]*n
for i in range(n):
    for j in range(n):
        rsum[i]+=mat[i][j]
        csum[j]+=mat[i][j]
res=[rsum[i]+csum[i] for i in range(n)]
print(" ".join(map(str,res)))
