# This is For Celsius to Fahrenheit conversion */
import os
temp = eval(input("Enter a temperature in Celsius: "))
print("In Fahrenheit, that is: ", 9/5*temp+32)

print("\n\n\n\n\n\n\n\n\n\n")

#This clears only the windows cmd
#### ===== os.system('cls')

# This is For finding the averave of some numbers */

num1 = eval(input("Number 1: "))
num2 = eval(input("Number 2: "))
set_of_numbers = [num1, num2]

addedNum = 3
repeater = input("Do you want to add more Numbers? Y/N")
if repeater == "N":
    x = True
else:
    x = False
    
while x == False:
    addIt = eval(input("Number: "))
    set_of_numbers.append(addIt)
    addedNum+1
    repeater = input("Do you want to add more Numbers? Y/N")
    if repeater == "N":
        x = True
    else:
        x = False

y = sum(set_of_numbers)
z = len(set_of_numbers)

print("The average of all the numbers added is: ", y/z)
