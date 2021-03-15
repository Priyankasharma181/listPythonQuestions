list=[[10,5,2],[15,2,5],[8,9,6]]
i=0
while i<len(list):
    j=0
    a =0
    while j<len(list[i]):
        a=a+list[i][j]
        j+=1
    i+=1
    print(a)        

    