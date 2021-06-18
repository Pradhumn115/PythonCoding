x=int(input("Enter How many lines Do you Want to Print?\n"))
r=int(input("1 for straight and 0 for reverse\n"))
y=bool(r)
i = 1
z=x

while(1):
    if y==True and i<=x :
        p=(i*"*")
        print(p)
        if i==x:
            break
        i=i+1




    elif y==False and z>=0:
        p = (z * "*")
        print(p)
        if z==0:
            break
        z = z - 1












