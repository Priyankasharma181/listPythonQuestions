list=[2,4,7,9,2,24,4,56,1]
i=0
a=[]
while i<len(list):
    j=0
    count=0
    while j<len(list):
        if list[i]==list[j]:
            count+=1
            a.append(list[i])
            print(list[i])
        j+=1
    # if list[i] in list:
       
    # a.append(list[i])
    # print(list[i])
    i+=1
print(list)    
           

           
        
    

