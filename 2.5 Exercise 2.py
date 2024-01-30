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
    if f < (height/2):
        space = " " * int((height/2) - f)
        print(space, "*" * m)
        m += 2
    elif f > height/2:
        if f == int(height/2) + 1:
            m -= 2
            if height % 2 == 0:
                print(space, "*" * m)
        m -= 2
        if height % 2 == 0:
            space = " " * int(x + 2)
        else:
            space = " " * int(x + 1)
        print(space, "*" * m)
        x += 1

# Number 15
A_height = int(input("Please type the height of the \"A\" (only numbers): "))
x0 = A_height
x1 = []
if A_height % 2 == 0:
    for o in range(A_height, 0, -1):
        if len(x1) == 0:
            print(" " * x0, "*")
            x0 -= 1
            x1.append("")
        elif o == int(A_height / 2):
            print(" " * x0, "*", " *" * int(A_height / 2))
            x0 -= 1
            x1.append(" ")
        else:
            print(" " * x0, "*_", *x1, "*")
            x0 -= 1
            x1.append(" ")
else:
    for b in range(A_height, 0, -1):
        if len(x1) == 0:
            print(" " * x0, "*")
            x0 -= 1
            x1.append("")
        elif b == int((A_height / 2) + 1):
            print(" " * x0, "*_", "* " * int(A_height/2))
            x0 -= 1
            x1.append(" ")
        else:
            print(" " * x0, "*", *x1, "*")
            x0 -= 1
            x1.append(" ")
