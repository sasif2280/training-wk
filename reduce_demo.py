from functools import reduce

ls=['21','34','56','78','11','14']

def add(num ,num2):
    return num+num2

sum= reduce(add,ls)
print(sum)