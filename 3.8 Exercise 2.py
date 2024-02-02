print("Number 9 B")
# Rewriting the code to denote AM or PM
start_hour = int(input("What time do you want to go?: "))
Period = 0
if start_hour < 13:
    Period = int(input("Press 1 for AM\nPress 2 for PM: "))

trip_hour = int(input("How many hours do you want to go?: "))


if Period == 2:
    start_hour = start_hour + 12

duration = start_hour + trip_hour
current_time = duration % 24

if current_time == 0:
    current_time = 12
    print("New Hour: ", current_time, "o'Clock AM")
elif current_time < 13:
    print("New Hour: ", current_time, "o'Clock AM")
else:
    current_time = current_time - 12
    print("New Hour: ", current_time, "o'Clock PM")

print("Number 10")
power = int(input("What power of two do you wish to get?: "))
power = str(power)
power2 = []

for i in range(len(power) + 1):
    