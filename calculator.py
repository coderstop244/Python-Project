#function for adding two numbers
def add(x,y):
    return x+y
#funtion for subtracting two numbers
def subtract(x,y):
    return x-y
#function for divinding two numbers
def divide(x,y):
    return x/y
#function for multiprication of two numbers
def multiply(x,y):
    return x*y

print("select operators")
print("1.add")
print("2.subtract")
print("3.divdide")
print("4.multiply")
    #Take input from the user
num1=float(input("Enter the first number:-"))
num2=float(input("Enter the second number:-"))
choice=int(input("Enterchoice:"))

if(choice==1):
    print("Addition:-",add(num1,num2))
elif(choice==2):
    print("Addition:-",subtract(num1,num2))
elif(choice==3):
    print("Addition:-",divide(num1,num2))
elif(choice==4):
    print("Addition:-",multiply(num1,num2))
else:
    print("Invalid Choice ")
