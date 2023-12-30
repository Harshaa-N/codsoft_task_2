def addition():
    add=num1+num2
    print("The addition of the given number is : ",add)
def subtraction():
    sub=num1-num2
    print("The  subtraction of the given number is : ",sub)
def multiplication():
    mul=num1*num2
    print("The  multiplication of the given number is : ",mul)
def division():
    div=num1/num2
    print("The division of the given number is : ",div)


print("************************************************************")
print("Arithmetic operation for the given number")
print("************************************************************")
num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number 2:"))
choice=int(input("Enter your choice:"))
if choice==1:
    addition()
elif choice==2:
    subtraction()
elif choice==3:
    multiplication()
elif choice==4:
    division()
else:
    print("INVALID CHOICE")
