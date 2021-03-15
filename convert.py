num=int(input("enter the num"))
a=[]
while num>0:
    num_1=int(input("enter the num "))
    a.append(num_1)
    num-=1
print(a) 
num_1=int(input("enter the num "))
i=0
while i<len(a):
    if num_1 in a:
        print("yes")
        break
    else:
        print("no")
        break
    i+=1


 
