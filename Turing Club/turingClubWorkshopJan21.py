##CTRL+SHIFT+B to run

##VARIABLES
a=2
b=4
print(a*b)

myString = "Hello World"

anotherString = ", my name is "
myName = "Amber!"

fullString = myString + anotherString + myName

print(fullString)

##LISTS
myList = [1,2,3]
anotherList = ['dog','cat','panda']

myList[0]
myList[1]

myNewString = "I have " + str(myList[0]) + " " + anotherList[2]
print(myNewString)

myList.append(4)

myNumbers = [8,9,10]
myList.extend(myNumbers)
print(myList)

##LOOPS
newList = []

for x in myList:
    newList.append(x*2)
print(newList)

##FUNCTIONS
name = "Amber"
age = 18

def NameAdder(x,y):
    nameAgeString = "Hi my name is {} and I'm {}".format(x,str(y))
    return nameAgeString

mySentence = NameAdder(name,age)
print(mySentence)

##READING DATA FROM A CSV
import pandas as pd

my_file = pd.read_csv("AAPL.csv")

df = pd.DataFrame(my_file)
df.head()
df['close']
d = df['close']
d[:5]
d[0:50:2]
col_open = df['open']

import numpy as np
np.mean(col_open)

ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/23/2019', periods = 1000))

##Plotting the data
import matplotlib.pyplot as pyplot
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

ts = ts.cumsum()
pyplot.plot(ts)
pyplot.show()
