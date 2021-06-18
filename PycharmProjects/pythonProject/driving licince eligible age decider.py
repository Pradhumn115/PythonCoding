x=int(input("enter your age\n"))
y=18
if x>y and x<100:
    print("eligible for driving\n")
elif x==y:
    print("cannot decide\n")
elif x>100 or x<7:
    print("enter a valid age")
else:
    print("not eligible for driving\n")