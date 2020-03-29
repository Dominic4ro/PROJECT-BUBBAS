import tkinter
from tkinter import *
from tkinter import messagebox

mainMenu = tkinter.Tk()
mainMenu.title("Main Menu")
mainMenu.geometry("1280x720")


# New Game Command
def n_game():
    # insert code to move to character selection screen
    print()


# Continue Game Command
def cont_game():
    loadFile = open("saveFile.txt", "r+")
    loadFile.readline()
    playerName = loadFile.readline()
    messagebox.showinfo("Hello There", "Welcome back, " + playerName + "\nLoading you back into the game now.")


# Code for the close window command attached to the exit Button
def close_window():
    mainMenu.destroy()


# Create Buttons for Main Menu
continue_game = tkinter.Button(mainMenu, text="Continue", command=cont_game, padx=75, pady=30)
new_game = tkinter.Button(mainMenu, text="New Game", padx=75, pady=30, command=lambda: n_game())
optionsButton = tkinter.Button(mainMenu, text="Options", padx=75, pady=30)
exitButton = tkinter.Button(mainMenu, text="Exit Game", command=close_window, padx=75, pady=30)

# Place Widgets
continue_game.place(x=550, y=300)
new_game.place(x=550, y=400)
optionsButton.place(x=550, y=500)
exitButton.place(x=550, y=600)


mainMenu.mainloop()
