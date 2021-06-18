def getdate():
    import datetime
    return datetime.datetime.now()





f=True

while(f==True):

    try:
        input1 = int(input("PRESS: \n1 for LOG\n2 for RETRIEVE Data\n"))
        if input1==1:
            input2 = int(input("Want to LOG?\nPRESS \n1 for FOOD\n2 for EXERCISE\n"))
            if input2==1:
                input3 = int(input("PRESS:\n1 for HARRY\n2 for ROHAN\n3 for HAMMAD\n"))

                if input3 == 1:
                    with open("Harryfood.txt", "a") as hf:
                        e = True
                        while (e == True):
                            input4 = input("Name of the food you ate\n")
                            hf.write("\n" + str(getdate()) + "\n" + "Food : " + input4 + "\n")
                            print("Done!")
                            e = bool(int(input("Do you want to enter more \nPRESS:\n1 for yes 0 for no: ")))
                            if e==False:
                                f = bool(int(input("Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))



                if input3 == 2:
                    with open("Rohanfood.txt", "a") as rf:
                        e = True
                        while (e == True):
                            input4 = input("Name of the food you ate\n")
                            rf.write("\n" + str(getdate()) + "\n" + "Food : " + input4 + "\n")
                            print("Done!")
                            e = bool(int(input("Do you want to enter more \nPRESS:\n1 for yes 0 for no ")))
                            if e == False:
                                f = bool(int(input(
                                    "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))


                if input3 == 3:
                    with open("Hammadfood.txt", "a") as haf:
                        e = True
                        while (e == True):
                            input4 = input("Name of the food you ate\n")
                            haf.write("\n" + str(getdate()) + "\n" + "Food : " + input4 + "\n")
                            print("Done!")
                            e = bool(int(input("Do you want to enter more \nPRESS:\n1 for yes 0 for no ")))
                            if e == False:
                                f = bool(int(input(
                                    "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))

            if input2==2:
                input3 = int(input("PRESS:\n1 for HARRY\n2 for ROHAN\n3 for HAMMAD\n"))

                if input3 == 1:
                    with open("Harryexercise.txt", "a") as he:
                        e = True
                        while (e == True):
                            input4 = input("Name of the exercise you Do\n")
                            he.write("\n" + str(getdate()) + "\n" + "Food : " + input4 + "\n")
                            print("Done!")
                            e = bool(int(input("Do you want to enter more \nPRESS:\n1 for yes 0 for no ")))
                            if e == False:
                                f = bool(int(input(
                                    "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))

                if input3 == 2:
                    with open("Rohanexercise.txt", "a") as re:
                        e = True
                        while (e == True):
                            input4 = input("Name of the exercise you Do\n")
                            re.write("\n" + str(getdate()) + "\n" + "Food : " + input4 + "\n")
                            print("Done!")
                            e = bool(int(input("Do you want to enter more \nPRESS:\n1 for yes 0 for no ")))
                            if e == False:
                                f = bool(int(input(
                                    "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))

                if input3 == 3:
                    with open("Hammadexercise.txt", "a") as hae:
                        e = True
                        while (e == True):
                            input4 = input("Name of the exercise you Do\n")
                            hae.write("\n" + str(getdate()) + "\n" + "Food : " + input4 + "\n")
                            print("Done!")
                            e = bool(int(input("Do you want to enter more \nPRESS:\n1 for yes 0 for no ")))
                            if e == False:
                                f = bool(int(input(
                                    "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))


        if input1==2:
            input2 = int(input("Want to RETRIEVE?\nPRESS \n1 for FOOD\n2 for EXERCISE\n"))
            if input2 == 1:
                input3 = int(input("PRESS:\n1 for HARRY\n2 for ROHAN\n3 for HAMMAD\n"))

                if input3 == 1:
                    with open("Harryfood.txt", "rt") as hr:

                        print(hr.read())
                        f = bool(int(input(
                            "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))

                if input3 == 2:
                    with open("Rohanfood.txt", "rt") as rr:
                        print(rr.read())
                        f = bool(int(input(
                            "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))

                if input3 == 3:
                    with open("Hammadfood.txt", "rt") as har:

                        print(har.read())
                        f = bool(int(input(
                            "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))

            if input2 == 2:
                input3 = int(input("PRESS:\n1 for HARRY\n2 for ROHAN\n3 for HAMMAD\n"))

                if input3 == 1:
                    with open("Harryexercise.txt", "rt") as her:
                        print(her.read())
                        f = bool(int(input(
                            "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))

                if input3 == 2:
                    with open("Rohanexercise.txt", "rt") as rer:
                        print(rer.read())
                        f = bool(int(input(
                            "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))

                if input3 == 3:
                    with open("Hammadexercise.txt", "rt") as haer:
                        print(haer.read())
                        f = bool(int(input(
                            "Do you want to go back to Main Menu?\nPRESS:\n1 for yes 0 for no and to exit: ")))

    except Exception as e:
        print(e)
        print("try again")
        continue






