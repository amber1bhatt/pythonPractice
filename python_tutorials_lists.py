##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py

#Lists can have strings, numbers, booleans...
friends = ["Kevin", "Karen", "Jim", "Bob", "Mary", "Martha"]
print(friends)
print(friends[0], friends[1], friends[2])

for i in range(0,3):
    print(friends[i])


print(friends[-1])
friends[1] = "Mike"
print(friends[1:])
print(friends[2:6])
