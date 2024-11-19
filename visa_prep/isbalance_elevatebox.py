def balance_arr(n,arr):
    totalsum=sum(arr)
    l_sum=0
    res=[]
    for i in range(n):
        r_sum=totalsum-l_sum-arr[i]
        val=abs(l_sum-r_sum)
        res.append(val)
        l_sum+=arr[i]
    return res
n=int(input())
arr=list(map(int,input().split()))
print(" ".join(map(str,balance_arr(n,arr))))
        
