import tkinter
from tkinter import *
from tkinter import messagebox

mainMenu = tkinter.Tk()
mainMenu.title("Main Menu")
mainMenu.geometry("1280x720")


# New Game Command
def n_game(playerName):
    saveFile = open("saveFile.txt", "w+")
    saveFile.write("Save 1")
    saveFile.write("\n")
    saveFile.write(playerName)
    messagebox.showinfo("Welcome to [PROJECT BUBBAS]",
                        playerName + " you will now be taken to the character selection screen.")
    saveFile.close()


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
new_game = tkinter.Button(mainMenu, text="New Game", padx=75, pady=30, command=lambda: n_game(playerName.get()))
optionsButton = tkinter.Button(mainMenu, text="Options", padx=75, pady=30)
exitButton = tkinter.Button(mainMenu, text="Exit Game", command=close_window, padx=75, pady=30)


# PlayerName Entry and Label
playerName = tkinter.Entry(mainMenu, font=18)
new_game_label = tkinter.Label(mainMenu, text="Start a New Game by Typing in a New Player Name: ")


# Place Widgets
continue_game.place(x=550, y=300)
new_game.place(x=550, y=400)
optionsButton.place(x=550, y=500)
exitButton.place(x=550, y=600)
playerName.place(x=423, y=400, relwidth=.1, relheight=.1151)
new_game_label.place(x=70,y=400,relwidth=.25, relheight=.1151)

mainMenu.mainloop()
