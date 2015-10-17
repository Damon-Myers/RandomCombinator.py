#!/usr/bin/python
 
from Tkinter import *
import random

combinationNum = 2
combinationList = []

#this recursive method finds companion things for a specified thing
##the things it picks as companions cannot be in the list of already picked things
def findCompanions(alreadyPicked, whole_list, number_needed):
    #Append the values that don't already exist into alreadyPicked array so that they can be saved.
    while(number_needed != 0):
        rand_int = random.randrange(0, len(whole_list))
        try:
            alreadyPicked.index(whole_list[rand_int])
        except ValueError:
            alreadyPicked.append(whole_list[rand_int])
            number_needed = number_needed - 1

    result = ''

    #concatenate the picked strings and return them
    for picked in alreadyPicked:
        result = result + picked + ' '

    return result


#this is the first function called to randomize our list of things
##It is called whenever the 'randomize' button is clicked
def Randomize():
    things = text.get(1.0, 'end-1c')
    if(things != ""):
        splitStr = things.split('\n')
        for string in splitStr:
            pickedItems = [string]
            temp = findCompanions(pickedItems, splitStr, combinationNum - 1)
            list.insert(END, temp)

#This function defines how many things will go into each combination
##It is called whenever the 'submit' button is clicked
def setNumber():
    #Declared the variable to be global, otherwise python creates a local var
    global combinationNum
    if(entry.get() == ''):
        combinationNum = 3
    else:
        combinationNum = int(entry.get())

#function used to clear the results list
def clearResults():
    list.delete(0, END)

#function that will delete the selected result
def deleteSelected():
    print(list.curselection())

#Set up the GUI last so that it has access to functions
root = Tk()
root.geometry('800x600')
root.wm_title("Combinator")

#Instantiation of widgets
textLabel = Label(root, text = "Input list:")
text = Text(root, height=30, width = 20)

rdm_button = Button(root, text = "Randomize", command = Randomize)

entry = Entry(root, text = "3")
submitBtn = Button(root, text = "Set Number of Items in Combinations", command = setNumber)

listLabel = Label(root, text = "Combinations:")
list = Listbox(root, height = 30, width = 60)

clearBtn = Button(root, text = "Clear", command = clearResults)

deleteBtn = Button(root, text = "Delete", command = deleteSelected)

#Place the widgets on the grid
entry.grid(column = 2, columnspan = 4, padx = 5, pady = 5, row= 0, rowspan = 1)
submitBtn.grid(column = 7, columnspan = 4, padx = 5, pady = 5, row= 0, rowspan = 1)

textLabel.grid(column = 2, columnspan = 4, padx = 5, pady = 5, row= 1, rowspan = 1)
text.grid(column = 0, columnspan = 10, padx = 5, pady = 5, row= 2, rowspan = 10)

listLabel.grid(column = 12, columnspan = 4, padx = 5, pady = 5, row= 1, rowspan = 1)
list.grid(column = 11, columnspan = 10, padx = 5, pady = 5, row= 2, rowspan = 10)

rdm_button.grid(column = 2, columnspan = 4, padx = 5, pady = 5, row= 14, rowspan = 1)
clearBtn.grid(column = 6, columnspan = 4, padx = 5, pady = 5, row= 14, rowspan = 1)

deleteBtn.grid(column = 10, columnspan = 4, padx = 5, pady = 5, row= 14, rowspan = 1)

root.mainloop()
