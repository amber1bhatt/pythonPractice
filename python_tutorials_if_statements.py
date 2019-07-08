##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py

is_male = True
is_tall = False
is_cool = True

if is_male or is_tall:
    print("You are a male or tall or both ")
elif is_male and not(is_tall):
    print("You are a short male")

else:
    print("You are neither male nor tall")
