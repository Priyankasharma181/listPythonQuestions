a=["priyanka","leena","salon","pinki","mahzbeen"]
new=[]
i=0
while i<len(a):
    j=0
    count=0
    while j<len(a[i]):
        count = count+1
        j = j+1
    if count%2==0:
        print(count)
    # else:
        #  print(count)
    i = i+1           
            
