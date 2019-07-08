##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py

def power_function(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result

print(power_function(3,7))
