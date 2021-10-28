myVar = input("Does it move? (yes/no) ")
if myVar == "yes":
    myNextVar = input("Should it move? (yes/no) ")
    if myNextVar == "yes":
        print("No problem")
    elif myNextVar == "no":
        print("Then use duct tape!")
    else:
        print("Answer my question! You didn't type yes or no.")
elif myVar == "no":
    myNextVar = input("Should it move? (yes/no) ")
    if myNextVar == "yes":
        print("Use WD40!")
    elif myNextVar == "no":
        print("No problem")
else:
    print("Answer my question! You didn't type yes or no.")
