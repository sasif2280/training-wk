list1 = [" ", " ", " "]
list2 = [" ", " ", " "]
list3 = [" ", " ", " "]

# list of all the lists
map = [list1, list2, list3]

position = input("enter the location of tressure\n")
row = int(position[0])
col = int(position[1])
map[row-1][col-1] = "@"


print(f"{list1}\n{list2}\n{list3}")
