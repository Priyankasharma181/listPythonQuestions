name=["k","r","i","t","i","t","k","a"]
# name=input("enter ")
# i=l
i = 0
j=0
a=[]
while i<len(name):
    if name[i]==name[-j]:
        a.append(name[i])
        i+=1
    j+=1
print(a)
if a==name:
    print("given num is palodrim")
else:
    print("is not palodrim")
# i=0
# j=len(name)-1
# while i<j:
#     if name[i]==name[j]:
#       i+=1
#       j+=1
#       print("given name is polidram")
#       break
#     else:
#       print("given no is not polidram")
#       break
    
    
