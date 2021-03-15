num=[700,78,9940,23,70,956,12,5,10120]
index=0
max=num[1]
while index<len(num):
    m=num[index]
    if m>max:
        max=m
    index+=1
print(max)
# num.remove(max)   
    