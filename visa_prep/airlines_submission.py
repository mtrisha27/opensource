x,n=list(map(int,input().split()))
no_of_passengers=x*100
plane_req=max(0,n-no_of_passengers)
print((plane_req+99)//100)
