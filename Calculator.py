n1 =int (input ("Enter forst number : "))
n2 = int (input ("Enter second number : "))
op = input("Enter operator : ")
match op:
 case '+' :
  out=n1+n2
  print(f"Addition of  {n1} and {n2} is {out}")
 case '-' :
  if (n1>n2):
   out = n1-n2
   print(f"Subtraction of {n1} and {n2} is {out}")
  else:
   out = n2 - n1
   print (f"Subtraction of {n2} and {n1} is {out}")
 case '*':
  out = n1 *n2
  print(f"Multiplication of {n1} and {n2}  is {out} ")
 case '/':
  if (n2==0):
   print(f"Division by zero not possible")
  else:
   out=n1/n2
   print(f"Division of {n1} by {n2} is : {out}")
 case _ : #default
   print("Invalid choice")
 