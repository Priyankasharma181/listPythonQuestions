# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
# i=0
# while i<len(marks):
#     max1=max(marks[i])
#     print(max1)
#     i+=1


marks=[[45,67,2,34,89],[56,78,23,45],[56,89,34,34]]
i=0
while i<len(marks):
    j=0
    b=marks[i][0]
    while j<len(marks[i]):
        if marks[j]>b:
            b=marks[j]
        j+=1
    print("maximum",b)
    i+=1


