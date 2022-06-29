ls=['21','34','56','78','11','14']

def adult(age):
    if int(age)>18:
        return age

#map will iterates with each and every item in the list
# so in output get some none values
adults=list(map(adult,ls))
print(adults)


#if we want to filter the list we can use filter function
newadults=list(filter(adult,ls))
print(newadults)