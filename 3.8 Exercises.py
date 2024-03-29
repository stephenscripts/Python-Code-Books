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
x = angle % 360
x = str(x) + "°"
print(x)

print("Number 8")
seconds = int(input("Please enter your time in seconds: "))
minutes = int(seconds/60)
second = seconds % 60
print("The Minute.Seconds conversion of: ", seconds, "seconds, is: ", minutes, "minutes", second, "seconds")

print("Number 9")

start_hour = int(input("How many hours do you want to go to (from 1 - 12 hours): "))
trip_hour = int(input("How many hours do you want to go?: "))
duration = start_hour + trip_hour
current_time = duration % 12

if current_time != 0:
    print("New Hour: ", current_time, "o'Clock")
else:
    current_time = 12
    print("New Hour: ", current_time, "o'Clock")
