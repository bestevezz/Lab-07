import datetime

#now.hour = float(input("What hour is it? (0-23) "))
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

if now.hour <= 5:
    print("It's early, you should be asleep")
elif now.hour <= 7:
    print("Wake up, have some coffee, run a mile, and eat")
elif now.hour <= 9:
    print("Time to go to work. :(")
elif now.hour <= 12:
    print("You should be working")
elif now.hour <= 13:
    print("Have some lunch!")
elif now.hour <= 17:
    print("Do you feel that afternoon lull?")
elif now.hour <= 19:
    print("Time to hit the gym")
elif now.hour <= 21:
    print("Time to eat dinner")
elif now.hour <= 23:
    print("get that sleep, and REPEAT!")
else:
    print("Thats not an hour of the day?(0-23)")
