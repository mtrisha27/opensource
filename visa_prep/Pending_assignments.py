x,y,z=list(map(int,input().split()))
total_time_req=x*y
total_time_avai=z*24*60
if total_time_req<=total_time_avai:
    print("YES")
else:
    print("NO")
