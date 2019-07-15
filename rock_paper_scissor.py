#simple rock paper game in python

import random




def rock_paper_scissor():
    choices = ['rock', 'paper', 'scissor']
    user_point = 0
    comp_point = 0
    print("+++++++++++++++Rock+++++++Paper+++++++Scissor++++++++++++++")


    for i in range(1,4): #iterating 3 round of game
        print("round ",i," of 3\n")

        #main menu
        user_input = int(input('Enter \n0 for rock\n1 for paper \n2 for scissor\n'))
        comp_choice = random.randint(0,2)


#while input is invalid ,prompt user again for valid input
        while user_input>2:
            user_input = int(input("invalid input,,\nEnter \n0 for rock\n1 for paper \n2 for scissor\n"))


#for valid input,game proceeds
        if user_input == comp_choice:
            print("you choose:",choices[user_input])
            print("comp choose:",choices[comp_choice])
            print("this round is a tie\n")

        if user_input == 0:
            if comp_choice == 1:
                comp_point += 1
                print("you choose:", choices[user_input])
                print("comp choose:", choices[comp_choice])
                print('comp won this round\n')

            elif comp_choice == 2:
                user_point += 1
                print("you choose:", choices[user_input])
                print("comp choose:", choices[comp_choice])
                print('user won this round\n')

        elif user_input == 1:
            if comp_choice == 0:
                user_point+=1
                print("you choose:", choices[user_input])
                print("comp choose:", choices[comp_choice])
                print('you won this round\n')

            elif comp_choice == 2:
                comp_point+=1
                print("you choose:", choices[user_input])
                print("comp choose:", choices[comp_choice])
                print('comp won this round\n')

        elif user_input == 2:
            if comp_choice == 0:
                comp_point+=1
                print("you choose:", choices[user_input])
                print("comp choose:", choices[comp_choice])
                print('comp won this round\n')

            elif comp_choice == 1:
                user_point+=1
                print("you choose:", choices[user_input])
                print("comp choose:", choices[comp_choice])
                print('you won this round\n')

        print("======================================================\n")


    #comparing user and computer point to decide who have won the game
    if user_point == comp_point:
        print("your point=",user_point)
        print("computer point=",comp_point)
        print("this game is tie")

    elif user_point>comp_point:
        print("your point=", user_point)
        print("computer point=", comp_point)
        print("you have won this game\n")

    else:
        print("your point=", user_point)
        print("computers point=", comp_point)
        print("computer have won this game\n")


#calling main function
rock_paper_scissor() 


#to restart the game

again=False

while not again:
    val = int(input("Enter 1 to play again or 0 to exit the game"))
    if val == 1:
        rock_paper_scissor()
    else:
        print('GOOD BYE')
        again = True



