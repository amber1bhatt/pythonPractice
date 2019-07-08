##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py

secret_word = "dog"
guess = ""
chances = 3

while guess != secret_word:
    guess = input("Enter a guess: ")
    print("You have " + str(chances) + " chances remaining")
    chances-=1
    if chances == -1 and guess != secret_word:
        print("You lose!")
        break
    elif chances >= -1 and guess == secret_word:
        print("You win!")
