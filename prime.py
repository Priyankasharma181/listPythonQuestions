m=[23,30,11,2,1,4,3]
i=0
while i<len(m):
    j=2
    k=0
    f=0
    while j<m[i]//2:
        if m[i]%j==0:
            f+=1
            break
        j+=1
if f==0:
    print(m[j],"prime")
else:
    print(m[j],"not prime")    