import random

# enter here the name of friends  separated by comma and space.
lst = input("names seperated comma{,}\n")

newlist = lst.split(", ")

payer = random.randint(0, len(newlist)-1)
print(f"\n todays bill will be payed by {newlist[payer]}")
