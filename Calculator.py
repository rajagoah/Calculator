def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num2-num1

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

if __name__=="__main__":

    while True:
       num1= int(input("Enter the first number: "))
       num2= int(input("Enter the second number: "))
       op = input("WHat operation do you want to perform? A for addition, S for subtraction, D for Division and M for multiplication")

       if op.lower()=='a' or (op.lower() == 'a' and response.lower() == 'y'):
           result = add(num1,num2)
           print("addition is: ", result)
           response = input("do you want to continue?? Y/N")
           if response.lower() == 'n':
               break
       elif op.lower() == 's'or (op.lower() == 's' and response.lower() == 'y'):
           result= sub(num1,num2)
           print("subtraction is: ", result)
           response = input("do you want to continue?? Y/N")
           if response.lower() == 'n':
               break
       elif op.lower() == 'd' or (op.lower() == 'd' and response.lower() == 'y'):
           result = div(num1,num2)
           print("division is: ", result)
           response = input("do you want to continue?? Y/N")
           if response.lower() == 'n':
               break
       elif op.lower() == 'm' or (op.lower() == 'm' and response.lower() == 'y'):
           result = mul(num1,num2)
           print("multiplication is: ", result)
           response = input("do you want to continue?? Y/N")
           if response.lower() == 'n':
               break
       else:
           print("you've entered the incorrect operation")