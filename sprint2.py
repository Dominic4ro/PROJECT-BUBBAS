import tkinter as t
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pygame as pg
pg.init()

# making the window
window = Tk()
window.title("Character Creation")
window.geometry('1920x1080')

plyrName = ""
gender = "male"
plyrRace = ""
plyrClass = ""
classBio = ""

def pyGame(playerName):

    #text
    font = pg.font.Font('MANDATOR.ttf', 32)
    nameText = font.render(playerName, False, (250, 250, 250))
    companionText = font.render("Bubba", False, (250, 250, 250))

    win = pg.display.set_mode((1280, 720))
    pg.display.set_caption("Project Bubbas")
    x = 64
    y = 64
    x2 = x - 64
    y2 = y
    width = 64
    height = 64
    vel = 5
    char1 = pg.image.load('red mage down.png')
    char2 = pg.image.load('warrior.png')

    # text to screen
    font = pg.font.SysFont(None, 25)

    def drawPlayArea():
        # draw area
        pg.draw.rect(win, (150, 160, 170), (0, 0, 1280, 512))
        # draw characters
        if y2 < y:
            win.blit(char2, (x2, y2))
            win.blit(char1, (x, y))
        else:
            win.blit(char1, (x, y))
            win.blit(char2, (x2, y2))
        # update display
        pg.display.update()

    run = True
    while run:
        #the press variable determines if a key has been pressed in this iteration of the loop
        press = False

        #time is delayed by 10 milliseconds each iteration of the loop regardless of which action is performed
        pg.time.delay(10)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            #keeps player in bounds
            if y > 0:
                #xt and yt are temporary variables to control companion's movement
                xt = x
                yt = y
                #for loop animates movement across one tile
                for count in range(0, 64):
                    #if statement checks to see if player and companion are at same Y coordinate
                    if y2 == yt:
                        #if the player and companion are at same Y coordinate, this if statement checks if companion is
                        #to the left or right of the player
                        if x2 < xt:
                            x2 += 1
                        else:
                            x2 -= 1
                    #if player and companion are at two different y coordinates, test for above or below
                    elif y2 > yt:
                        y2 -= 1
                    else:
                        y2 += 1
                    #player's vertical position goes 8 up, 8 times to reach one 64 pixel block
                    y -= 1
                    #drawPlayArea is called each loop in order to do the animation
                    drawPlayArea()
                    pg.time.delay(5)
                pg.time.delay(50)
                press = True

        if keys[pg.K_a]:
            if not press:
                if x > 0:
                    yt = y
                    xt = x
                    for count in range(0, 64):
                        # if statement checks to see if player and companion are at same X coordinate
                        if x2 == xt:
                            # if the player and companion are at same Y coordinate, this if statement checks if
                            # companion is above or below the player
                            if y2 < yt:
                                y2 += 1
                            else:
                                y2 -= 1
                        # if player and companion are at two different x coordinates, test for left or right
                        elif x2 > xt:
                            x2 -= 1
                        else:
                            x2 += 1
                        # player's vertical position goes 8 up, 8 times to reach one 64 pixel block
                        x -= 1
                        drawPlayArea()
                        pg.time.delay(5)
                    pg.time.delay(50)
                    press = True

        if keys[pg.K_s]:
            if not press:
                if y < 448:
                    xt = x
                    yt = y
                    for count in range(0, 64):
                        # if statement checks to see if player and companion are at same Y coordinate
                        if y2 == yt:
                            # if the player and companion are at same Y coordinate, this if statement checks if companion is
                            # to the left or right of the player
                            if x2 < xt:
                                x2 += 1
                            else:
                                x2 -= 1
                        # if player and companion are at two different y coordinates, test for above or below
                        elif y2 > yt:
                            y2 -= 1
                        else:
                            y2 += 1
                        # player's vertical position goes 8 up, 8 times to reach one 64 pixel block
                        y += 1
                        drawPlayArea()
                        pg.time.delay(5)
                    pg.time.delay(50)
                    press = True

        if keys[pg.K_d]:
            if not press:
                if x < 1216:
                    yt = y
                    xt = x
                    for count in range(0, 64):
                        # if statement checks to see if player and companion are at same X coordinate
                        if x2 == xt:
                            # if the player and companion are at same Y coordinate, this if statement checks if companion is
                            # above or below the player
                            if y2 < yt:
                                y2 += 1
                            else:
                                y2 -= 1
                        # if player and companion are at two different x coordinates, test for left or right
                        elif x2 > xt:
                            x2 -= 1
                        else:
                            x2 += 1
                        # player's vertical position goes 8 up, 8 times to reach one 64 pixel block
                        x += 1
                        drawPlayArea()
                        pg.time.delay(5)
                    pg.time.delay(50)
                    press = True

        drawPlayArea()

        #draw bar
        win.blit(char1, (20, 530))
        win.blit(char2, (350, 530))
        win.blit(nameText, (100, 540))
        win.blit(companionText, (430, 540))

        pg.display.update()

    pg.quit()

# Functions for when buttons are pressed
def Back():
    messagebox.showinfo('Go Back', 'Temporary Box\nWill go back to the main menu')

# Gender selection
def Gender():
    if cboGender.get() == "Male":
        plyrGender = "male"
    if cboGender.get() == "Female":
        plyrGender = "female"
    return plyrGender


# race selection
def Race():
    if cboRace.get() == "Human":
        plyrRace = "human"

    elif cboRace.get() == "Elf":
        plyrRace = "elf"

    elif cboRace.get() == "Dwarf":
        plyrRace = "dwarf"

    elif cboRace.get() == "Orc":
        plyrRace = "orc"
    return plyrRace

# output for Fin()
def ClassMsg():
    if cboClass.get() == "Wizard":
        plyrClass = "wizard, you are an offensive\nmagic type user that can only be\nused at range. You have with\nmeduim armor capabilites."

    elif cboClass.get() == "Knight":
        plyrClass = "knight, you are able to wear\nbigger, heavier armor (including shields)\nand weaponry, possibly sacrificing speed\nin favor of more defense and power."

    elif cboClass.get() == "Assassin":
        plyrClass = "assassin, you are a more\noffensive rogue, who sacrifices\ntechnical expertise for better stealth\nand killing abilities."

    elif cboClass.get() == "Priest":
        plyrClass = "priets, you are a squishy\ndedicated healer with little abilities\nat offense aside from specific types\nof enemies."

    elif cboClass.get() == "Archer":
        plyrClass = "archer, you are a weaker\nclass with very light armor. Your\nattacks are strong at range but weak\nup close."
    return plyrClass


# class for info for n_game()
def pClass():
    if cboClass.get() == "Wizard":
        plyrClass = "wizard"

    elif cboClass.get() == "Knight":
        plyrClass = "knight"

    elif cboClass.get() == "Assassin":
        plyrClass = "assassin"
    elif cboClass.get() == "Priest":
        plyrClass = "priets"

    elif cboClass.get() == "Archer":
        plyrClass = "archer"
    return plyrClass


# outputs the selected info onto the screen
def Fin():
    playerName = str(txtName.get())
    lblBio = Label(window, text="")
    lblBio = Label(window,
                   text="Your name is " + playerName + ".\nYou are a " + Gender() + " " + Race() + " just\nwaiting for an adventure.\nAs a " + ClassMsg(),
                   font=("Arial Bold", 25)).place(x=400, y=450)
    # btnContinue["state"] = NORMAL


# saves data to file
def n_game(txtName):
    saveFile = open("saveFile.txt", "w+")
    saveFile.write("Save 1")
    saveFile.write("\n")
    saveFile.write(txtName)
    saveFile.write("\n")
    saveFile.write(Race())
    saveFile.write("\n")
    saveFile.write(pClass())
    saveFile.write("\n")
    messagebox.showinfo("Welcome to [PROJECT BUBBAS]", txtName + ", you will now be taken on an adventure.")
    window.destroy()
    playerName = str(txtName)
    pyGame(playerName)
    saveFile.close()



# Getting the player's name
lblName = Label(window, text="Enter Your Character's Name:", font=("Arial Bold", 30)).place(x=400, y=30)
txtName = t.Entry(window, width=25, font=("Arial", 20))
txtName.place(x=980, y=38)

# Getting the player's gender
lblGender = Label(window, text="What is your character's gender?", font=("Arial Bold", 25)).place(x=1200, y=150)
cboGender = Combobox(window, font=("Arial", 20), values=["Male", "Female"], state="readonly")
cboGender.place(x=1290, y=250)
cboGender.current(0)
# btnMGender = t.Button(window, text="Male", bg="blue", fg="black", font=("Arial", 20), width=10, height=2, command=Male).place(x=1285, y=220)
# btnFGender = t.Button(window, text="Female", bg="pink", fg="black", font=("Arial", 20), width=10, height=2, command=Female).place(x=1485, y=220)


# Getting the player's race
lblRace = Label(window, text="Choose your character's race?", font=("Arial Bold", 25)).place(x=1220, y=400)
cboRace = Combobox(window, font=("Arial", 20), values=["Human", "Elf", "Dwarf", "Orc"], state="readonly")
cboRace.place(x=1290, y=500)
cboRace.current(0)

# Getting the player's class
lblClass = Label(window, text="Choose your character's class?", font=("Arial Bold", 25)).place(x=1218, y=650)
cboClass = Combobox(window, font=("Arial", 20), values=["Wizard", "Knight", "Assassin", "Priest", "Archer"],
                    state="readonly")
cboClass.place(x=1290, y=750)
cboClass.current(0)

# Dynamic Bio of player's choices
lblBio = Label(window, text="Character Bio", font=("Arial Bold", 35)).place(x=400, y=400)

# Buttons to go back to main menu or continue with the game
btnBack = t.Button(window, text="Back", bg="grey25", fg="white", font=("Arial", 20), width=12, height=2,
                   command=Back).place(x=600, y=900)
btnFinal = t.Button(window, text="Finalize", bg="grey25", fg="white", font=("Arial", 20), width=12, height=2,
                    command=Fin).place(x=850, y=900)
btnContinue = t.Button(window, text="Continue", bg="grey25", fg="white", font=("Arial", 20), width=12, height=2,
                       command=lambda: n_game(txtName.get()))
btnContinue.place(x=1100, y=900)

window.mainloop()

# event for button
# def clicked():
# res = "Welcome to " + txtName.get()
# lblName.configure(text=res)


# button
# bt = t.Button(window, text="Enter", bg="yellow", fg="blue", command=clicked).grid(column=1, row=0)

# combobox
# combo = Combobox(window)
# combo['values'] = (1, 2, 3, 4, 5, "Text")
# combo.current(3)
# combo.grid(column=0, row=0)

# messagebox
# messagebox.showinfo('Message title', 'Message content')



