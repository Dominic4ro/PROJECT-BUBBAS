import tkinter
import os
import io
import sys

newOrLoad = 'x'

while newOrLoad.lower() != 'n' and newOrLoad.lower() != 'c' and newOrLoad.lower() != 'w':
   newOrLoad = input("Would you like to start a new game or continue? Enter 'n' or 'c'")

if newOrLoad == 'w':
   clearFile = open("C:\\Users\\Student\\Desktop\\saveFile.txt", "w+")
   clearFile.write("no save")
   print("\nDebug mode enabled\n\nSave file wiped")
   sys.exit()

if newOrLoad == 'c':
   loadFile = open("C:\\Users\\Student\\Desktop\\saveFile.txt", "r+")
   if loadFile.readline() == 'no save':
       print("There was no file to load. Starting new game.")
       newOrLoad = 'n'
   else:
       playerName = loadFile.readline()
       print("Welcome back, " + playerName + "\nLoading you back into the game now.")




if newOrLoad == 'n':
   playerName = input("What is your name? ")
   saveFile = open("C:\\Users\\Student\\Desktop\\saveFile.txt", "w+")
   saveFile.write("Save 1")
   saveFile.write("\n" + playerName)
   print("Welcome to [PROJECT BUBBAS]," + playerName + "\nYou will now be taken to the character selection screen.")

