list1 = [" ", " ", " "]
list2 = [" ", " ", " "]
list3 = [" ", " ", " "]

# list of all the lists
map = [list1, list2, list3]

position = input("enter the location of tressure\n")
pos1 = int(position[0])
pos2 = int(position[1])

row = map[pos1-1]
row[pos2-1] = "@"


print(f"{list1}\n{list2}\n{list3}")
