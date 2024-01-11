import os
import time
# Number 1
print("*******************\n" * 4)
time.sleep(5)
os.system("cls")

# Number 2
print("*******************\n")
print("*                 *\n" * 2)
print("*******************\n")
time.sleep(5)
os.system("cls")

# Number 3
x = 1
y = "*"
z = [y]
while x < 5:
    print(*z)
    z.append(y)
    x += 1
print("")

time.sleep(5)
os.system("cls")
# Number 4
print((512-282)/(47.48 + 5))
time.sleep(5)
os.system("cls")

# Number 5
a = eval(input("Enter a number: "))
print("The square of", a, "is", a*a, ".", sep=" ")
time.sleep(5)
os.system("cls")

# Number 6
ex = eval(input("Enter a number: "))
print(ex, 2*ex, 3*ex, 4*ex, 5*ex, sep=" --- ")
time.sleep(5)
os.system("cls")

# Number 7
kg = eval(input("Enter a number Kilograms: "))
pounds = kg * 2.2
print(kg, "Kilogram is equivalent to ", pounds, "pounds", sep=" ")

time.sleep(5)
os.system("cls")

# Number 8
a1 = eval(input("Enter the first a number: "))
a2 = eval(input("Enter the second a number: "))
a3 = eval(input("Enter the third a number: "))
total = a1 + a2 + a3
average = total/3
print("Total:", total, "\n")
print("Average:", average)
time.sleep(5)
os.system("cls")

# Number 9
price = eval(input("Enter the Price: "))
tip = eval(input("Enter the Tip: \n"))
total = price + tip
print("Price:", price)
print("Tip:", tip)
print("Total:", total)
time.sleep(5)
os.system("exit")
