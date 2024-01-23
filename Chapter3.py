from random import randint
groups = []
Title = "Here are the list of Groups"
print(Title.capitalize())
for i in range(1, 101):
    w = i%7
    if w == 0:
        w = 7
        words = "Group: " + str(w) + "\n"
    else:
        words = "Group: " + str(w) + "\n"
    groups.append(words)

print(*groups)
