###############################################################################################
#    -----   ______   ------        |        --------   --------   -------
#   |_____  |      | |______|       |       |        | |        | |_______|
#   |       |______| |     \        |______ |________| |________| |
###############################################################################################
import time

# for variable name in range( number of times to repeat ):
#     statements to be repeated.

a = 0
for x in range(100000):
    s = time.perf_counter()
    k = [a]
    if x == 99999:
        print("The start time: ", s)
        print("The final time is: ", time.perf_counter())


for i in range(4):
    if i == 0:
        print("* " * 5)
    elif i == 1 or i == 2:
        print("*", "-----", "*")
    else:
        print("* " * 5)
    if i == 3:
        for y in range(4, 0, -1):
            print("* " * y)

for u in range(4):
    if u == 0:
        print("* " * 5)
    elif u == 1 or u == 2:
        print("*", "/////", "*")
    else:
        print("* " * 5)
    if u == 3:
        for l in range(4, 0, -1):
            print("* " * l)
            