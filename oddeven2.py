list=[12,45,56,99,89]
i=0
a=0
b=0
# even=[]
# odd=[]
while i<len(list):
    if list[i]%2==0:
        a=a+list[i]
        # even.append(list[i])
    else:
        b+=list[i]
        i+=1
print(a) 
print(b)


