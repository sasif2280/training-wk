# reverse the date format
lst = ['21-2-2001', '21-9-1003']


def get(dob):
    return (dob.split('-')[2], dob.split('-')[1], dob.split('-')[0])


# map takes a function and a list and returns a list
# its arguments are funcrtion and iterable items
pyob = list(map(get, lst))

# map returns a objects so we need to convert it to list
print(pyob)
