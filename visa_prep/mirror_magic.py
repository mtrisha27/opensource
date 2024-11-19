n=int(input())
mat=[list(map(int,input().split())) for i in range(n)]
for r in mat:
    r.reverse()
for r in mat:
    print(" ".join(map(str,r)))
