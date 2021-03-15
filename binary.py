binary_number = [1,0,0,1,1,0,1,1] 
i=0
length=len(binary_number)-1
sum=0
while i<len(binary_number):
    A=binary_number[length]
    B=(2**i)*A
    length-=1
    i+=1
    sum+=B
print(sum)    
     
          
        
     