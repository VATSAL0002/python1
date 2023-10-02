x = 5
y = 10

print(x == y)
print(x != y)
print(x >= y)
print(x <= y)
print(x > y)
print(x < y)


# logical operator
# and operator
a = 10
b = 15
print(x < y and a < b)
# or operator
print(x > y or a > b)
# not operator
print(not x != y)

# membership operators
str = "Vatsal"
print('v' in str)

b = [10,20,30,40]
print(20 in b)
print(50 not in b)

# identity operators
print( x is y)   
# (x==y)

print(x is not y)
# (x!=y)


# bitwise operator

c = 10
d = 8

print(bin(c))
print(bin(d))

print(c & d,bin(c&d))
print(c | d,bin(c|d))
print(c ^ d,bin(c^d))