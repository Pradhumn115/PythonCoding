while (True):
    l1 = ["+", "-", "x", "/"]
    x = int(input("Please select a operator (+,-,x,/)\npress 1 for +, press 2 for -, press 3 for x, press 4 for /\n"))
    print(l1)
    y = int(input("Please select a number 1\n"))
    z = int(input("Please select a number 2\n"))
    if x == 3 and y == 45 and z == 3:
        print("555")
    elif x == 1 and y == 56 and z == 9:
        print("77")
    elif x == 4 and y == 56 and z == 6:
        print("4")
    elif x == 1:
        print(y + z)
    elif x == 2:
        print(y - z)
    elif x == 3:
        print(y * z)
    elif x == 4:
        print(y / z)
    else:
        print("try again")




