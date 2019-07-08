##CTRL + SHIFT + B to Run

 ##Printing backslash and quortation mark
print("This is \ a \"string")

##Concatonating strings (appending)
phrase = "Good Memes"
print(phrase + " are good")

##Converting lower and uppcase
print(phrase.lower())
print(phrase.upper())

##Check for lower and uppercase
print(phrase.islower())

##Converting to upper then checking
print(phrase.upper().isupper())

##Length of a string
print(len(phrase))

##Grabbing individual characters
print(phrase[0])
print(phrase[1])
print(phrase[2])
print(phrase[3])

##Index function (gives index of where the first instance of the character/string appears)
print(phrase.index("G"))

##Replace function
print(phrase.replace("Good", "Great"))

##Reading data from a CSV file
import pandas as pd
my_file = pd.read_csv("AAPL.csv")
df = pd.DataFrame(my_file)
i = 10
print(df[:i+1])
