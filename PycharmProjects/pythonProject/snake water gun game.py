import random
'''1 for snake 2 for water 3 for gun'''


r=True
while(r==True):
    chances = 10
    points = 0
    points1 = 0

    print("Welcome to the Game\nSnake Water Gun")
    print("Total Chances : 10")
    try:
        while(True):

            l1 = ["Snake", "Water", "Gun"]
            x = random.choice(l1)

            if chances==0 and points1>points:
                print("Computer Won!")
                print("You Lost: You are Looser")
                print(f"Computer Points : {points1}")
                print(f"Your Points : {points}")
                r=bool(int(input("Do you want To play again?\nPress\n1 for YES 0 for NO\n")))
                if r==True:
                    break
                else:
                    break


            elif chances==0 and points>points1:
                print("You Won!")
                print("Computer Lost: Computer is a Looser")
                print(f"Your Points : {points}")
                print(f"Computer Points : {points1}")
                r = bool(int(input("Do you want To play again?\nPress\n1 for YES \n0 for NO\n")))
                if r==True:
                    break
                else:
                    break
            elif chances==0 and points==points1:
                print("Tie!!!")
                r = bool(int(input("Do you want To play again?\nPress\n1 for YES \n0 for NO\n")))
                if r == True:
                    break
                else:
                    break


            input1 = input("Press\ns for Snake\nw for Water\ng for Gun\n")
            chances = chances - 1

            if input1=="s":
                if input1=="s" and x=="Water":
                    points=points+1
                    points1 = points1-1
                    print(f"Snake ~~ {x}")
                    print(f"Snake drank the Water\nPoint : +1\nTotal Points: {points}\nChances left: {chances} ")
                    print(f"Computer Points : {points1}")


                if input1=="s" and x=="Gun":
                    points=points-1
                    points1 = points1+1
                    print(f"Snake ~~ {x}")
                    print(f"Snake was Shot by the Gun\nPoint : -1\nTotal Points: {points}\nChances left: {chances} ")
                    print(f"Computer Points : {points1}")

                if input1=="s" and x=="Snake":
                    points=points-0
                    print(f"Snake ~~ {x}")
                    print(f"Both are Same\nNothing Happened!\nTotal Points: {points}\nChances left: {chances} ")
                    print(f"Computer Points : {points1}")

            if input1=="w":
                if input1 == "w" and x == "Snake":
                    points = points - 1
                    points1 = points1 + 1
                    print(f"Water ~~ {x}")
                    print(f"Snake drank the Water\nPoint : -1\nTotal Points: {points}\nChances left: {chances} ")
                    print(f"Computer Points : {points1}")

                if input1 == "w" and x == "Gun":
                    points = points + 1
                    points1 = points1 - 1
                    print(f"Water ~~ {x}")
                    print(f"Gun Sank in Water\nPoint : +1\nTotal Points: {points}\nChances left: {chances} ")
                    print(f"Computer Points : {points1}")

                if input1 == "w" and x == "Water":
                    points = points - 0
                    print(f"Water ~~ {x}")
                    print(
                        f"Both are Same\nNothing Happened!\nTotal Points: {points}\nChances left: {chances} ")
                    print(f"Computer Points : {points1}")

            if input1=="g":
                if input1 == "g" and x == "Snake":
                    points = points + 1
                    points1 = points1 - 1
                    print(f"Gun ~~ {x}")
                    print(f"Snake was shot by Gun\nPoint : +1\nTotal Points: {points}\nChances left: {chances} ")
                    print(f"Computer Points : {points1}")

                if input1 == "g" and x == "Water":
                    points = points - 1
                    points1 = points1 + 1
                    print(f"Gun ~~ {x}")
                    print(f"Gun Sank in Water\nPoint : -1\nTotal Points: {points}\nChances left: {chances} ")
                    print(f"Computer Points : {points1}")

                if input1 == "g" and x == "Gun":
                    points = points - 0
                    print(f"Gun ~~ {x}")
                    print(
                        f"Both are Same\nNothing Happened!\nTotal Points: {points}\nChances left: {chances} ")
                    print(f"Computer Points : {points1}")


    except Exception as e:
        print(e)
        print("try again")
        continue

