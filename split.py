a="{}(){()([]"
b=a.split(" ")
i=0
while i<len(b):
    j=1
    list=[]
    while j<len(b):
        if b[i]==b[-j]:
            list.append(b)
        else:
            
        j+=1
    i+=1  
print(list)             


