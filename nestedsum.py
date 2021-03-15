list = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
i=0
a=0
while i<len(list):
    b=0
    j=0
    while j<len(list[i]):
        a=a+list[i][j]
        j+=1
    i+=1
    print(a)  
              