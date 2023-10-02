for i in range(1,20,2):
    print(i)


for i in range(1,11):
    print("2*" , i , "=" , 2*i)



for i in range(10,0,-1):
    print(i)

cars = ["mustang","supra","gtr","porche"]
for x in cars:
    print(x)
    if x == "supra":
        break

name = ["vatsal","parth","ravi","mehul"]
for i in name:
    print(i)
    if name == "ravi":
        continue


for i in range(1,20,3):
    print(i)

for i in range(20,0,-3):
    print(i)


beast = ["mustang","supra","gtr","porche"]
driver = ["vatsal","parth","ravi","mehul"]

for i in beast:
    for j in driver:
        print(i,j)