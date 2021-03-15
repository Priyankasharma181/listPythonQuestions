list=[2,8,6,7,9,3,54,0,1]
i=0
while i<len(list):
    if list[i]%2==0:
        print("even")
    else:
        print("odd")
    i+=1
    print(list[i])