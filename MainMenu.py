

import tkinter
from tkinter import messagebox


mainMenu = tkinter.Tk()
mainMenu.title("Main Menu")
mainMenu.geometry("1280x720")

#No Game File Error Message for no game to continue
def no_game_file_err():
    messagebox.showinfo("No Game File to Continue", "No Game File to Continue...Please Start a New Game")
#Code for the close window command attached to the exit Button
def close_window():
    mainMenu.destroy()

#Create Buttons for Main Menu
continue_game = tkinter.Button (mainMenu,text = "Continue", command = no_game_file_err, padx=75, pady=30)
new_game = tkinter.Button(mainMenu,text = "New Game", padx=75, pady=30)
optionsButton = tkinter.Button(mainMenu,text = "Options", padx=75, pady=30)
exitButton = tkinter.Button(mainMenu,text = "Exit Game", command = close_window, padx=75, pady=30)

#Place buttons
continue_game.place(x=550, y=300)
new_game.place(x=550, y=400)
optionsButton.place(x=550, y=500)
exitButton.place(x=550, y=600)

#Pack Buttons
#continue_game.pack(padx=100, pady=10)
#new_game.pack(padx=10, pady=0)
#optionsButton.pack(padx=10, pady=10)
#exitButton.pack(padx=10, pady=10)


mainMenu.mainloop()
