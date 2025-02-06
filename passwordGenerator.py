import tkinter as tk, random, string
from tkinter import messagebox

#Creates a toggled button for adding special character requirement to the password
def specialCharacterToggleButton():
    global specialCharacter_is_on
    specialCharacter_is_on = not specialCharacter_is_on
    if specialCharacter_is_on:
        specialCharacter_toggle_button.config(bg = "green")
    else:
        specialCharacter_toggle_button.config(bg="red")

#Creates a toggle button for adding number requirement to the password
def numberToggleButton():
    global number_is_on
    number_is_on = not number_is_on
    if number_is_on:
        number_toggle_button.config(bg = "green")
    else:
        number_toggle_button.config(bg = "red")

#Create the password with the requirements and passes it back to the label to show the user
def printPassword():
    password = number_specialGenerator()
    passwordVar.set(password)
    password_label.config(textvariable=passwordVar)

#Function used to create the password
def number_specialGenerator():
    #generates a random number to decide how many special characters/numbers to add
    #Checks the minimum number of characters required and if no value is set, sets the minimum characters to 8
    if minCharactersEntry.get() == "":
        minLength = 8
    else:
        minLength = minCharactersEntry.get()
        minLength = int(minLength)

    #Checks the minimum number of numbers required and if no value is set, sets the minimum to 0
    if minNumberEntry.get() == "":
        minCount = 0
    else:
        minCount = minNumberEntry.get()
        minCount = int(minCount)
    
    #Checks the minimum number of special characters required and if no value is set, sets the minimum to 0
    if minSpecialEntry.get() == "":
        minSpecialCount = 0
    else:
        minSpecialCount = minSpecialEntry.get()
        minSpecialCount = int(minSpecialCount)
    #Variables to hold the amount of numbers and special characters added to the generated password
    numberCount = 0
    specialCount = 0
    password = ""
    # A loop that checks if the length of the password matches the min length requirement and if not continues generating characters
    while len(password) < minLength:
        char = randomPick()
        if char.isdigit():
            numberCount += 1
        elif char in string.punctuation:
            specialCount += 1
        #Append the character to the generated password
        password += char
    #If the generated password doesnt have a number or special character then it will add one to meet the requirements
    while numberCount < minCount and specialCount < minSpecialCount:
        if number_is_on and numberCount <= minCount:
            password += addNumber()
        elif specialCharacter_is_on and specialCount == 0:
            password+= addSpecialCharacter()
    return password

#Returns a number 0-9 to add to the password
def addNumber():
    return str(random.randint(0,9))

def addSpecialCharacter():
    return random.choice(string.punctuation)
#Function to randomly pick a character,special character or number
def randomPick():
        rand = random.randint(1,4)
        if rand == 1 or rand == 2:
            #Returns a random letter
            return random.choice(string.ascii_letters)
        elif rand == 3:
            #Returns a random number 0-9
            return str(random.randint(0,9))
        else:
            #Gets a string of all punctuation characters and returns one a random
            return random.choice(string.punctuation)
        
#Create the GUI
gui = tk.Tk()
gui.title("Super Safe Password Generator")
gui.geometry("600x600")

passwordVar = tk.StringVar()
#Button Frame
button_frame = tk.Frame(gui)
button_frame.pack(side = "top")
button_frame2 = tk.Frame(gui)
button_frame2.pack(side = "bottom")

#Create button for special characters
specialCharacter_is_on = False
specialCharacter_toggle_button = tk.Button(button_frame, text="Special Character", command=specialCharacterToggleButton, bg="red")
specialCharacter_toggle_button.pack(side="left", padx=10)

#Create button for numbers
number_is_on = False
number_toggle_button = tk.Button(button_frame, text="Number", command=numberToggleButton, bg="red")
number_toggle_button.pack(side="right", padx=10)

#Create a button to generate password
passwordGeneratorButton = tk.Button(button_frame2, text="Generate Password", command=printPassword)
passwordGeneratorButton.pack(side="bottom", pady = 10)

#Labels
password_label_frame = tk.Label(gui)
password_label_frame.pack(side = "bottom")
password_label = tk.Label(password_label_frame, textvariable=passwordVar)
password_label.pack(side="top", pady=100)

entry_label_frame = tk.Label(gui)
entry_label_frame.pack(side="top")
minCharactersLabel = tk.Label(entry_label_frame, text="Minimum number of characters: ")
minCharactersLabel.pack(pady=5)
minCharactersEntry = tk.Entry(entry_label_frame, width=30)
minCharactersEntry.pack(padx=10)

numberLabel = tk.Label(entry_label_frame, text="How many numbers: ")
numberLabel.pack(pady=5)
minNumberEntry = tk.Entry(entry_label_frame, width=30)
minNumberEntry.pack(padx=10)

specialLabel = tk.Label(entry_label_frame, text= "How many special characters: ")
specialLabel.pack(pady=5)
minSpecialEntry = tk.Entry(entry_label_frame, width=30)
minSpecialEntry.pack(padx=10)

gui.mainloop()