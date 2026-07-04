#adding while loop to loop again to not stop the program
while True:
 #this is the first variable to store value
  a=float(input("Enter a 1st number:"))
  #this is the second variable to store value
  b=float(input("Enter a 2nd number:"))
  #asking user what operation to use
  operation=input("Select a operation +,-,/,* :")
  #if user selects + it will add the the variable a and b
  if operation == "+":
   print(a+b)
   print(" \n--------------------------------------------------")
   #if user selects - it will subtract the the variable a and b
  elif operation=="-":
   print(a-b)
   print("\n--------------------------------------------------")
   #if user selects * it will multiply the the variable a and b
  elif operation=="*":
   print(a*b)
   print("\n --------------------------------------------------")
   #if user selects / it will divide the the variable a and b
  elif operation=="/":
   #adding a safety if statement suppose if user try to divide by zero the program crashes and throws a "ZeroDivisionError"
   if b==0:
    print("The denominator cant be zero try a different number")
   else: 
    print(a/b)
    print("\n --------------------------------------------------")
   #if user selects none of the available options it will display a error
  else:
   print("sorry your selected operation is invalid")
   print(" \n--------------------------------------------------")

