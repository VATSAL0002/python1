att = int(input("enter the attendence : "))
held = int(input("enter the absent : "))

per = round((att / (att + held)*100))
print(per)
if per >= 75 :
    print ("Allowd")
else :
    print("Not Allowed")