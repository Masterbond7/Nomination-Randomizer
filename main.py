"""Name: Nomination Randomizer v2.2
   Author: James Slough
   Date: 05/03/2020"""
# Importing Libraries
from tkinter import * # Importing everything from tkinter
from tkinter import messagebox # Importing messagebox from tkinter (because if I don't it will say that messagebox isn't defined)
import secrets # Import secrets for randomization function


# Defineing function to draw random names
def drawRandom():
    # Get Input from text fields
    names = NameArea.get("1.0", END).split("\n")[:-1] # Get names from name field and separate by new line (and saving the values in a list) ignoring the last newline character
    reasons = ReasonArea.get("1.0", END).split("\n")[:-1] # Get the reasons for the nominations from the reason field and separate by new line (and saving the values in a list) ignoring the last newline character
    nominators = NominatorArea.get("1.0", END).split("\n")[:-1] # Get the name of the nominators from the nominators field and separate by new line (and saving the values in a list) ignoring the last newline character
    # Getting the number of people to choose and if it is not an integer give a suitable error message
    try: numberOfPeople = int(PeopleNumArea.get("1.0", END))
    except: messagebox.showerror("Randomizer Error", "The amount of people to draw must be an integer (no decimal point).")

    # Checking if the amount of data in each column is the same, and if it is not displaying a suitable error message
    if (not(len(names) == len(reasons))) or (not(len(reasons) == len(nominators))):
        messagebox.showerror("Dataset Error", "The amount of data in each column is not the same.") # Displaying the error message
    # If the amount of data in each column is the same rearange the data into a list containing lists that have the students name, the reason they were nominated, and then who nominated them
    else:
        allPeople = [] # Initializing the array where all of the data from the spreadsheet will be stored
        # Rearanging the data and appending it to the array
        for personIndex in range(len(names)):
            allPeople.append([names[personIndex], reasons[personIndex], nominators[personIndex]]) # Appending a list with all of the data about the person to the main list
    
    # Getting the random choices            
    finalPeople = [] # Initializing the list that the people drawn will be appended to
    # For every person you want to get it chooses a random person and removes them from the allPeople list so they don't get drawn multiple times
    for i in range(numberOfPeople):
        finalPeople.append(allPeople.pop(allPeople.index(secrets.choice(allPeople))))

    # Opening a popup window with the results
    output = "" # Initialize a string that will be put in the popup window that contains the results
    for personData in finalPeople:
        output += "{person}: {reason} - {nominator}\n".format(person=personData[0], reason=personData[1], nominator=personData[2]) # For every person that has been selected add the data to a string that will be displayed as the output
    resultWindow = Toplevel() # Initializing the window
    resultWindow.geometry("400x300") # Setting the size of the window
    resultWindow.iconbitmap("superMario.ico") # Setting the window icon
    resultWindow.title("Results") # Setting the window title
    resultWindow.resizable(False, False) # Stopping the window from being resized by the user
    resultBox = Text(resultWindow) # Creating the results box inside the results window
    resultBox.place(x=10, y=10, width=380, height=280) # Place the results box inside the results window with a 10 pixel boarder on each side
    resultBox.insert(END, output) # Put the output string in the results box

    # Save the output string in a text file called output.txt
    outputFile = open("output.txt", "w") # Load the text file we want to write to
    outputFile.write(output) # Write the data to the text file
    outputFile.close() # Save the changes to the text file

# Defineing a function to save the current data to dataset.csv
def saveFunc():
    # Get Input from text fields
    names = NameArea.get("1.0", END).split("\n")[:-1] # Get names from name field and separate by new line (and saving the values in a list) ignoring the last newline character
    reasons = ReasonArea.get("1.0", END).split("\n")[:-1] # Get the reasons for the nominations from the reason field and separate by new line (and saving the values in a list) ignoring the last newline character
    nominators = NominatorArea.get("1.0", END).split("\n")[:-1] # Get the name of the nominators from the nominators field and separate by new line (and saving the values in a list) ignoring the last newline character

    # Checking if the amount of data in each column is the same, and if it is not displaying a suitable error message
    if (not(len(names) == len(reasons))) or (not(len(reasons) == len(nominators))):
        messagebox.showerror("Dataset Error", "The amount of data in each column is not the same.") # Displaying the error message
    # If the amount of data in each column is the same then save to dataset.csv
    else:
        outFile = open("dataset.csv", "w") # Load the csv file we want to write to
        # For every person format the data so it can be stored in the csv file
        for i in range(len(names)):
            outStr = "{0},{1},{2}".format(names[i], reasons[i], nominators[i]) # Formatting the data
            outFile.write("{0}\n".format(outStr)) # Saving the data in the csv file
        outFile.close() # Saving the changed file

# Defining a function to load from the file dataset.csv
def loadFunc():
    inFile = open("dataset.csv", "r") # Open the csv file we want to read from
    names = "" # Define an empty string for the loaded names to be saved into
    reasons = "" # Define an empty string for the loaded reasons to be saved into
    nominators = "" # Define an empty string for the loaded nominators to be saved into

    # For every line in the csv file save the data into the corresponding strings
    for line in inFile:
        names += "{0}\n".format(line.strip("\n").split(",")[0]) # Adding the loaded names to the names string
        reasons += "{0}\n".format(line.strip("\n").split(",")[1]) # Adding the loaded reasons to the reasons string
        nominators += "{0}\n".format(line.strip("\n").split(",")[2]) # Adding the loaded nominators to the nominators string

        # Deleting the current data in the input boxes and replacing it with the newly loaded data
        NameArea.delete("1.0", END) # Deleting the data in the name input box
        ReasonArea.delete("1.0", END) # Deleting the data in the reason input box
        NominatorArea.delete("1.0", END) # Deleting the data in the nominator input box
        NameArea.insert(END, names[:-1]) # Setting the data in the name input box to the new name data and removing the last newline character
        ReasonArea.insert(END, reasons[:-1]) # Setting the data in the reason input box to the new reason data and removing the last newline character
        NominatorArea.insert(END, nominators[:-1]) # Setting the data in the nominator input box to the new nominator data and removing the last newline character

# Defining a function to clear the data in the input boxes
def clearFunc():
    NameArea.delete("1.0", END) # Deleting the data in the name input box
    ReasonArea.delete("1.0", END) # Deleting the data in the reason input box
    NominatorArea.delete("1.0", END) # Deleting the data in the nominator input box

# Initializing TKinter
window = Tk() # Creating the window
window.title("Nomination Randomizer") # Setting the window title
window.iconbitmap("superMario.ico") # Setting the window icon
width = 600 # Setting the width variable
height = 450 # Setting the height variable
window.geometry("{0}x{1}".format(width, height+20)) # Setting the width and height to the width variable and to the height variable plus 20 (to add space for the menu at the top)
sX = width/400 # Setting the scale x variable to the current width divided by the original width
sY = height/300 # Setting the scale y variable to the current height divided by the original height
window.resizable(False, False) # Stopping the window from being resized by the user

# Initializing the menu
menu = Menu(window) # Creating a new menu on the main window
dataset_menu = Menu(menu, tearoff=0) # Creating a new tab for the menu
dataset_menu.add_command(label="Save", command=saveFunc) # Adding the save button to the dropdown menu
dataset_menu.add_command(label="Load", command=loadFunc) # Adding the load button to the dropdown menu
dataset_menu.add_command(label="Clear", command=clearFunc) # Adding the clear button to the dropdown menu
menu.add_cascade(label="Dataset", menu=dataset_menu) # Naming the dropdown menu Dataset
window.config(menu=menu) # Setting this custom menu as the menu

# Creating and placing the things on the main window
# Creating the name area
NameArea = Text(window) # Creating the name input box
NameArea.place(x=10*sX, y=25*sY, height=200*sY, width=120*sX) # Placing the name input box and scaling
NameAreaLabel = Label(window, text="Student name:", font="Arial {0}".format(int(8*sY))) # Creating the label for the name input box
NameAreaLabel.place(x=10*sX, y=2.5*sY) # Placing and scaling the label for the name input box
# Creating the reason area
ReasonArea = Text(window) # Creating the reason input box
ReasonArea.place(x=140*sX, y=25*sY, height=200*sY, width=120*sX) # Placing the reason input box and scaling
ReasonAreaLabel = Label(window, text="Reason for nomination:", font="Arial {0}".format(int(8*sY))) # Creating the label for the reason input box
ReasonAreaLabel.place(x=140*sX, y=2.5*sY) # Placing and scaling the label for the reason input box
# Creating the nominator area
NominatorArea = Text(window) # Creating the nominator input box
NominatorArea.place(x=270*sX, y=25*sY, height=200*sY, width=120*sX) # Placing and scaling the nominator input box
NominatorAreaLabel = Label(window, text="Name of the nominator:", font="Arial {0}".format(int(8*sY))) # Creating the label for the nominator input box
NominatorAreaLabel.place(x=270*sX, y=2.5*sY) # Placing and scaling the label for the nominator input box
# Creating the people number area
PeopleNumArea = Text(window, font="Arial {0}".format(int(10*sY))) # Creating the people number input box
PeopleNumArea.place(x=10*sX, y=245*sY, height=20*sY, width=380*sX) # Placing and scaling the people number input box
PeopleNumAreaLabel = Label(window, text="Number of people to draw:", font="Arial {0}".format(int(8*sY))) # Creating the label for people number input box
PeopleNumAreaLabel.place(x=10*sX, y=225*sY) # Placing and scaling the label for the people number input box
# Creaing the randomize button
RandomizeButton = Button(window, text="Randomize", command=drawRandom) # Creating the randomize button
RandomizeButton.place(x=165*sX, y=270*sY, height=25*sY, width=70*sX) # Placing and scaling the randomize button
RandomizeButton['font'] = "Arial {0}".format(int(8*sY)) # Scaling the randomize button text

# Main loop to keep the window constantly updating
window.mainloop()
