# we will doing all our task in this program using function
# this program is used to cheked the number is even or not
# from randomly generated list of numbers
def even_no(lis):
    lis2 = []
    for i in lis:
        if(i % 2 == 0):
            lis2.append(i)
            break  # if even no is there then just break the loop
    return lis2


lis = [1, 12, 3, 4, 8, 6, 5]


# fubction is used to extract even numbers from the list of numbers
def append_even(lis2):
    lis3 = []
    for i in lis:
        if(i % 2 == 0):
            lis3.append(i)
            continue
    return lis3


lis = [1, 12, 3, 4, 8, 6, 5]

# calling the function 1
lis2 = even_no(lis)
print("first even numbers is occured:", lis2)

# calling function 2
lis3 = append_even(lis)
print("list of even no is:", lis3)
