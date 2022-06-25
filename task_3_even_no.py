#this program is used to cheked the number is even or not
#from randomly generated list of numbers

lis=[1,12,3,4,8,6,5]
lis2=[]
for i in lis:
    if(i%2==0):
        lis2.append(i)
        break   #if even no is there then just break the loop
print("first even numbers is occured:",lis2)