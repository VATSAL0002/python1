# mutable data type
    # list
    # dictionery
    # byte array

# immutable data types
    # int 
    # float 
    # complex 
    # string
    # string 
    # tuple 
    # set 

a = 10
print(a,type(a))

b = 10.5
print(b,type(b))

c = 2+3j
print(c,type(c))

str = "vatsal"
print(str,type(str))

str2 = '"vatsal patel"'
print(str2,type(str2))

# lists are mutable

list = [1,82,2.2,"vatsal"]
list[2] = "patel"
print(list,type(list))

# tuple is faster than list ]
# tuple must contain more than one value  
# tuple is immutable

tuple = (58,96.6,"mehul")
print(tuple,type(tuple))



# Dictionaries are used to store data values in key:value pairs
# dictionary is mutable 
d1 = {
    'fname' : 'vatsal',
    'lname' : 'patel'
}
# print(d1,type(d1))
# print(d1["fname"])
# print(len(d1))
d1.update({'fname':'ankit'})
d1.update({'mname' : 'pravinkumar'})
print(d1)

# set is mutable 
s = {10,20,30,10}
print(s,type(s))