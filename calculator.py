number_1 = int(input("Give me a number, any number... "))
number_2 = int(input("Great, now another one "))
operation = (input("What opeartion do u want? (mul, div, mod) "))
if (operation == "mul"):
    print(number_1 * number_2)
elif (operation == "div"):
    print(number_1 / number_2)
elif (operation == "mod"):
    print(number_1 % number_2)
else:
    print("Don't overcomplicate things, it's my first calculator")
