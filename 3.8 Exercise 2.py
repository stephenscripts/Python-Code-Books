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

print("Number 10A")
power = int(input("What power of two do you wish to get?: "))
Power_of_two = 2 ** power
print("The last digit is: ", Power_of_two % 10)

print("Number 10B")
power = int(input("What power of two do you wish to get?: "))
Power_of_two = 2 ** power
if power < 100:
    print("The last digit is: ", "0" * int(len(str(Power_of_two)) - len(str(Power_of_two % 100))), Power_of_two % 100)
else:
    print("The last digit is: ", Power_of_two % 100)

print("Number 10C")
power = int(input("What power of two do you wish to get?: "))
Digits = int(input("How many last digists do you want: "))
Power_of_two = 2 ** power