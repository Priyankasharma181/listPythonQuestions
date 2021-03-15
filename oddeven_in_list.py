list=[2,8,6,7,9,3,54,0,1]
i=0
a=[]
b=[]
while i<len(list):
    if list[i]%2==0:
       a.append(list[i])
    else:       
        b.append(list[i])
    i+=1
print(a,b)    
