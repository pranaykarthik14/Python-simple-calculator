def add(x,y):
  return x+y
def substract(x,y):
  return x-y
def multiple(x,y):
  return x*y
def divide(x,y):
  if y !=0:
    return x/y
  else :
    return "Error! division by zero." 

def calculator():
  print("Simple Calculator")
  print("choose operation:")
  print("1.add")
  print("2.subraction:")
  print("3.multiple:")
  print("4.divide:")
  while True :
     choice= input("Enter choice (1/2/3/4):")
     if choice in ['1','2','3','4']:
       num1 = float(input("Enter first number :"))
       num2 = float(input("Enter second number :"))
       if choice == '1':
          print(f"The result is : {add(num1,num2)}")
       elif choice == '2':
          print(f"The result is : {subract(num1,num2)}")
       elif choice == '3':
          print(f"The result is : {multiple(num1,num2)}")
       elif choice == '4':
          print(f"The result is : {divide(num1,num2)}")
       next_calculation = input("Do you want to perform another calculation?(yes/no):")
       if next_calculation.lower()!='yes':
            break

  else:
           print("Invalid Input")
#run the calculator
calculator()
