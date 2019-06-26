###GENERAL EXAMPLE OF WHILE AND FOR LOOP###

#while (x == 1):
  #some code will repeat until x does not equal 1
print (5 % 50)

'''
+
-
*
**
/
%
'''
#for i in range (1,10,3):
  #some code will repeat until i reaches 10
  #i will begin at 1
  #i will increase by 3 at the end of each loop

###INSTRUCTIONS###
#Ask the user to input a range of numbers
#Using a loop, print out every other even number in that range

###OBSERVATIONS/TIPS###
#I think the mod (%) operator is a great idea to check if a number is odd or even. Perhaps the comparison between first/second number is what needs to be changed.
#Bear in mind the user can pick ANY number they wish -- even very high ones.
#You really only need one loop, but  if statements are definitely needed

'''
print ("write a range of numbers")
first_number = input ("write the first number in the range")
second_number = input ("write the second number in the range")
if int(first_number) % int(second_number) == 1 :
  first_number = int(first_number) - 1
for i in range (int(first_number), int(second_number), 4):
  print(i)
  '''
