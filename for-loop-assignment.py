print ("write a range of numbers")
first_number = int(input ("write the first number in the range"))
second_number = int(input ("write the second number in the range"))
if first_number % 2 == 0:
  for i in range (int(first_number), int(second_number) + 1, 4):
    print (str(i))
else:
  first_number = first_number + 1
for i in range (int(first_number), int(second_number) + 1, 4):
    print (str(i))
