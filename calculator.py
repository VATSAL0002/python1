def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y == 0:
        return "can't divide by zero"
    return x/y

# x = float(input("enter the value of x : "))
# y = float(input("enter the value of y : "))

print("please select the option")
print("a.add")
print("b.sub")
print("c.mul")
print("d.div")

choice = input("please enter choice (a/b/c/d) : ")

x = float(input("enter the value of x : "))
y = float(input("enter the value of y : "))

if choice == 'a':
    print(x, " + ", y, " = " ,add(x,y))

elif choice == 'b':
    print(x, " - ", y ," = ",sub(x,y))   

elif choice == 'c':
    print(x, " * ", y ," = ",mul(x,y))   

elif choice == 'd':
    print(x, " / ", y ," = ",div(x,y))   

else:
    print("invalid input")

# def main():
#     add()
#     sub()
#     mul()
#     div()

# print("please enter yes or no : ")

# if == 'yes':
#     main()
# else
#     break
