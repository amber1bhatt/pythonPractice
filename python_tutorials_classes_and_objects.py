##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py

from classes_example import Student

student1 = Student("Jim", "Business", 3.1, False) #Student Object (objects are instances of a class)
student2 = Student("Pam", "Art", 2.5, True)
print(student1.gpa)
print(student2.gpa)
