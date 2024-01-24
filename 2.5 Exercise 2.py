# Number 12
height = int(input("Please type the height of the star-triangle (only numbers): "))
for i in range(1, height+1):
    print("*"*i)

# Number 13
height = int(input("Please type the height of the star-triangle (only numbers): "))
for i in range(height, 0, -1):
    print("*"*i)

# Number 14
height = int(input("Please type the height of the Diamond-triangle (only numbers): "))
m = 1
x = 0
for f in range(height + 1):
    if f < height/2:
        space = " " * int((height/2) - f)
        print(space, "*" * m)
        m += 2
    elif f > height/2:
        m -= 2
        space = " " * int(x)
        print(space, "*" * m)
        x += 1
