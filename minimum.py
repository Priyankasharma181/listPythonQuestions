lst = [99,1.2,45,0,8,54,67,2,5]
b= lst[0]
i=0
while(i<len(lst)):
    if lst[i] < b:
        b = lst[i]
    i+=1
print(b)





