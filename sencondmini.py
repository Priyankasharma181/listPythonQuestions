list=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
max=list[0]
secmax=list[1]
i=0
while i<len(list):
    if list[i]>max:
        secmax=max
        max=list[i]
    elif list[i]>secmax:
        secmax=list[i]
    i+=1
print(" sechighest list is =",secmax)    
        
        
            

        


