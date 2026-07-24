n, k = map(int, input().split())
li = list(map(int, input().split()))
cc = li[k-1]
c = 0
for sc in li:
    if sc>=cc and sc>0:
        c += 1  
print(c) #pls submit
 
     
    