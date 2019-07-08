##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py

from mc_quiz_class_example import Question

question_prompts = [
    "Color of apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "Color of bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "Color of strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)
