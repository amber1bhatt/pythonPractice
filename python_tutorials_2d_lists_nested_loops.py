##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py

num_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(num_grid[2][2])

for row in num_grid:
    for col in row:
        print(col)
