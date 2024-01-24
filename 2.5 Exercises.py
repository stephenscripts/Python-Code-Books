from decimal import getcontext
getcontext().prec = 1000
# Number 1
for i in range(101):
    print("Nnamani Stephen")

# Number 2
print("Nnamani Stephen " * 10, end=" ")

# Number 3
for i in range(101):
    print(i, "Nnamani Stephen", sep=". ")

# Number 4
for i in range(21):
    print(i, i*i, sep=". ")

# Number 5
for i in range(8, 90, 3):
    print(i)

# Number 6
for i in range(100, 0, -2):
    print(i)

# Number 7
output = []
for i in range(0, 10):
    output.append("A")
for j in range(0, 8):
    output.append("B")
for k in range(1, 9):
    if k%2 != 0:
        output.append("C")
    else:
        output.append("D")
for l in range(0, 8):
    if l == 0:
        output.append("E")
    elif l == 7:
        output.append("G")
    else:
        output.append("F")

print(*output)

# Number 8
name = input("Type your name here: ")
name = name + "\n"
x = 0

try:
    Number_of_Times = int(input("How many times do you want your name printed: "))
except NameError:
    print("Please you must type in a NUMBER eg 8")
    x += 1
if Number_of_Times < 1:
    print("Please type in numbers between 1 to 5000")
    x += 1
else:
    print(name*Number_of_Times)

# The Errors are not handled properly, moving to the next question

# Number 9
fibonacci = int(input("How many Fibonacci Numbers do you want printed?: "))
k = [1]
m = 0
for f in range(fibonacci-1):
    if len(k) < 2:
        k.append(m + k[-1])
        m = m + k[-1]
    else:
        k.append(k[-1] + k[-2])

print(*k)

# Number 10
height = int(input("Please type the height of * (only numbers): "))
width = int(input("Please type the width of * (only numbers): "))

for a in range(height):
    print("*"*width)


# Number 11
height = int(input("Please type the height of * (only numbers): "))
width = int(input("Please type the width of * (only numbers): "))

for a in range(height):
    if a == 0 or a == height-1:
        print("*"*width)
    else:
        gap = width-2
        print("*" + " "*gap + "*")
