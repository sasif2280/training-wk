#extract even numbers from the list of numbers
#using continue
lis=[1,12,3,4,8,6,5]
lis2=[]
for i in lis:
    if(i%2==0):
        lis2.append(i)
        continue
print("first even numbers is occured:",lis2)

