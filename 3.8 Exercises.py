import random

print("Number 1:")
x = []
for i in range(51):
    x.append(random.randint(3, 6))
print(*x)

print("Number 2:")
x = random.randint(1, 50)
y = random.randint(2, 5)
print(x, "^", y, ": ", x**y)

print("Number 3:")
x = random.randint(1, 10)
print("Stephen " * x)

print("Number 4")
x = round(random.uniform(1.00, 10.00), 2)
print(x)

print("Number 5")
y = 1
for i in range(2, 52):
    print("#", y, ": ", random.randint(1, i), "( Generates between 1 and ", i, ")")
    y += 1

print("Number 6")
x = int(input("Please enter your first number: "))
y = int(input("Please enter your second number: "))
print(abs(x-y)/(x+y)) # abs() returns the absolute value of a computation

print("Number 7")
angle = int(input("Please enter your angel from -180 to 180: "))
if angle % 180 == 0:
    if angle == -180:
        print()


