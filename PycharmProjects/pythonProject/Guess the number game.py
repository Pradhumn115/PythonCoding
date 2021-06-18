import random

r=True
while (r==True):
    x = random.randint(1, 100)
    z = 9
    print("The NUMBER GUESS!!!", "\nGUESS THE NUMBER##")
    print("Total Chances:", z)
    while(True):

        try:

            if z == 0:
                print("Game Over")
                print("The Number was:", x)
                r=bool(int(input("Do you want to play again?\nPress\n1 for yes \n0 for no\n")))
                if r==True:
                    break
                else:
                    break

            print("Chances left:", z)
            y = int(input("Enter Number:-\n"))

            if y > x :
                print("Enter a Smaller Number")

            elif y < x :
                print("Enter a Greater Number")


            elif y == x :
                z = z - 1
                print("Congratulations you entered the right number", "\nThe Number was", x)
                print("You took", 9 - z, "Chances")
                r = bool(int(input("Do you want to play again?\nPress\n1 for yes \n0 for no\n")))
                if r == True:
                    break
                else:
                    break

            z = z - 1

        except :
            print("ERROR:Only integers allowed")
            continue












