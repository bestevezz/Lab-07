import datetime

usertime = float(input("What hour is it? (0-23) "))

if usertime <= 5:
    print("It's early, you should be asleep")
elif usertime <= 7:
    print("Wake up, have some coffee, run a mile, and eat")
elif usertime <= 9:
    print("Time to go to work. :(")
elif usertime <= 12:
    print("You should be working")
elif usertime <= 13:
    print("Have some lunch!")
elif usertime <= 17:
    print("Do you feel that afternoon lull?")
elif usertime <= 19:
    print("Time to hit the gym")
elif usertime <= 21:
    print("Time to eat dinner")
elif usertime <= 23:
    print("get that sleep, and REPEAT!")
else:
    print("Thats not an hour of the day?(0-23)")
