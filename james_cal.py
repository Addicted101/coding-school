print("Welcome to my simple, efficient calculator!/n")
print("Please select an operation:")
print("Addition (+) /nSubtraction (-) /Multiplication (*) /nDivision (/)")
operand = input("Your choice: ")
number1 = input("\nFirst number: ")
number2 = input("\nSecond number: ")

if operand == "+":
  print(str(number1) + " " + operand + " " + str(number2) + " = " + str(float(number1) + float(number2)))

elif operand == "-":
  print(str(number1) + " " + operand + " " + str(number2) + " = " + str(float(number1) - float(number2)))

elif operand == "*":
  print(str(number1) + " " + operand + " " + str(number2) + " = " + str(float(number1) * float(number2)))

elif operand == "/":
  print(str(number1) + " " + operand + " " + str(number2) + " = " + str(float(number1) / float(number2)))
