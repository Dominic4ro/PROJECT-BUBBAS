import tkinter as t
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pygame as pg
import random

pg.init()

mainMenu = tkinter.Tk()
mainMenu.title("Main Menu")
mainMenu.geometry("1280x720")


def pyGame(playerName):
    def battle(self):
        a = len(self.enemies)
        n = len(self.fighters)
        i = 0
        p = 0
        m = 0
        q = 0
        player_spot = 0
        companion_spot = 0
        eH1 = self.enemies[0].health
        print(eH1)
        eH2 = self.enemies[1].health
        eH3 = self.enemies[2].health

        # draw arena
        win.blit(dungeonArena, (0, 0))
        playerDefense = pg.transform.scale(pg.image.load('elf mage right.png').convert_alpha(), (80, 90))
        playerTurn = pg.transform.scale(pg.image.load('elf.png').convert_alpha(), (80, 90))
        compDefense = pg.transform.scale(pg.image.load('elf knight right.png').convert_alpha(), (80, 90))
        compTurn = pg.transform.scale(pg.image.load('elf knight down.png').convert_alpha(), (80, 90))
        win.blit(playerDefense, (300, 180))
        pg.draw.rect(win, (2, 2, 2), (0, 450, 1280, 280))

        def drawPlayerStats():

            # redraw section
            pg.draw.rect(win, (2, 2, 2), (0, 450, 250, 280))

            # draw icons
            win.blit(playerDown, (22, 480))
            win.blit(compDown, (22, 620))

            # render and draw text for names and HP
            win.blit(nameText, (100, 480))
            pHP = smallFont.render("HP: " + str(self.fighters[player_spot].health), False, (250, 250, 250))
            win.blit(pHP, (100, 520))
            win.blit(companionText, (100, 610))
            cHP = smallFont.render("HP: " + str(self.fighters[companion_spot].health), False, (250, 250, 250))
            win.blit(cHP, (100, 650))

            # update display
            pg.display.update()

        def drawEnemyStats():

            # redraw section
            pg.draw.rect(win, (2, 2, 2), (830, 450, 450, 270))

            # if there are three enemies
            if a == 3:

                # draw enemy icons
                win.blit(enemy1, (910, 470))
                win.blit(enemy1, (910, 550))
                win.blit(enemy1, (910, 630))

                # draw enemy health bars
                pg.draw.rect(win, (250, 250, 250), (1000, 480, 250, 35))
                pg.draw.rect(win, (250, 250, 250), (1000, 560, 250, 35))
                pg.draw.rect(win, (250, 250, 250), (1000, 640, 250, 35))

                # calculate enemy health
                e1HP = (self.enemies[0].health * 250) / eH1
                print(str(int(e1HP)))
                e2HP = (self.enemies[1].health * 250) / eH2
                print(str(e2HP))
                e3HP = (self.enemies[2].health * 250) / eH3
                print(str(e3HP))

                # draw enemy health
                if self.enemies[0].health > 0:
                    pg.draw.rect(win, (250, 20, 20), (1000, 480, int(e1HP), 35))
                if self.enemies[1].health > 0:
                    pg.draw.rect(win, (250, 20, 20), (1000, 560, int(e2HP), 35))
                if self.enemies[2].health > 0:
                    pg.draw.rect(win, (250, 20, 20), (1000, 640, int(e3HP), 35))

            pg.display.update()

        def drawMoves():

            # draw section
            pg.draw.rect(win, (2, 2, 2), (250, 450, 580, 270))

            # assign current fighter's moves to text renders
            turn = myFont.render("It's " + str(z.name[:-1]) + "'s Turn!", False, (250, 250, 250))
            ap = smallFont.render(str(z.action_points - p) + " Action Points Remain", False, (250, 250, 250))
            move1 = smallFont.render(str(z.move1.name), False, (250, 250, 250))
            move2 = smallFont.render(str(z.move2.name), False, (250, 250, 250))
            move3 = smallFont.render(str(z.move3.name), False, (250, 250, 250))
            move4 = smallFont.render(str(z.move4.name), False, (250, 250, 250))
            move5 = smallFont.render("End Turn", False, (250, 250, 250))
            move6 = smallFont.render("Items", False, (250, 250, 250))

            # draw text to screen
            win.blit(turn, (375, 460))
            win.blit(ap, (377, 505))
            win.blit(move1, (275, 575))
            win.blit(move2, (455, 575))
            win.blit(move3, (635, 575))
            win.blit(move4, (275, 650))
            win.blit(move5, (455, 650))
            win.blit(move6, (635, 650))

            # assign parameters for selected move
            if m < 4:
                selectY = 565
            else:
                selectY = 640

                68 / 9 + 8

            if m == 1 or m == 4:
                selectX = 260
            elif m == 2 or m == 5:
                selectX = 440
            else:
                selectX = 620

            # draw select box
            win.blit(selectBox, (selectX, selectY))

            # update display
            pg.display.update()

        def drawTarget():

            # draw section
            pg.draw.rect(win, (2, 2, 2), (250, 450, 600, 270))

            # draw move name
            selectedMove = myFont.render(str(selected_move_name), False, (250, 250, 250))
            win.blit(selectedMove, (375, 575))

            # assign Y value to arrow
            if d == 0:
                arrowY = 480
            elif d == 1:
                arrowY = 560
            else:
                arrowY = 640

            # draw arrow
            win.blit(arrow, (800, arrowY))

            # update display
            pg.display.update()

        def drawMiss():

            # redraw background
            pg.draw.rect(win, (2, 2, 2), (250, 450, 600, 270))

            # draw text
            missText = myFont.render("THE ATTACK MISSED!", False, (250, 250, 250))
            win.blit(missText, (400, 530))

            # update display
            pg.display.update()

            # wait for 3 seconds
            pg.time.delay(3000)

        def drawEnemyAttack():

            # draw section
            pg.draw.rect(win, (2, 2, 2), (250, 450, 580, 270))

            # display current enemy's turn
            turn = myFont.render("It's " + str(z.name) + "'s Turn!", False, (250, 250, 250))
            win.blit(turn, (355, 470))

            # update display and delay by 1s
            pg.display.update()
            pg.time.delay(1000)

            # display enemy's attack
            attack = myFont.render(str(z.name) + " used " + str(selected_move.name), False, (250, 250, 250))
            win.blit(attack, (320, 575))

            # update display and delay by 2s
            pg.display.update()
            pg.time.delay(2000)

        def drawPlayerHit():

            # redraw background
            pg.draw.rect(win, (2, 2, 2), (250, 450, 600, 270))

            # draw text
            hitText = myFont.render(str(self.fighters[player_spot].name[:-1]) + " was hit!", False, (250, 250, 250))
            win.blit(hitText, (400, 530))

            # redraw player stats
            drawPlayerStats()

            # wait for 2 seconds
            pg.time.delay(2000)

        def drawCompanionHit():

            # redraw background
            pg.draw.rect(win, (2, 2, 2), (250, 450, 600, 270))

            # draw text
            hitText = myFont.render(str(self.fighters[companion_spot].name[:-1]) + " was hit!", False, (250, 250, 250))
            win.blit(hitText, (400, 530))

            # redraw player stats
            drawPlayerStats()

            # wait for 2 seconds
            pg.time.delay(2000)

        def drawArena():

            # redraw background
            win.blit(dungeonArena, (0, 0))

            # if it is the player's turn
            if z.isPlayer():
                win.blit(playerTurn, (300, 180))
                win.blit(compDefense, (250, 300))
            # if it is the companion's turn
            elif z.isCompanion():
                win.blit(playerDefense, (300, 180))
                win.blit(compTurn, (250, 300))

            # update display
            pg.display.update()

        # Orders Fighters by Speed
        for i in range(n):
            for j in range(0, n - i - 1):
                if int(self.fighters[j].speed) < int(self.fighters[j + 1].speed):
                    self.fighters[j], self.fighters[j + 1] = self.fighters[j + 1], self.fighters[j]
        while q < len(self.fighters):
            if self.fighters[q].isPlayer():
                player_spot = q
            if self.fighters[q].isCompanion():
                companion_spot = q
            q += 1

            # draw player stats
            drawPlayerStats()

            # draw enemy stats
            drawEnemyStats()

            pg.display.update()

            selectBox = pg.image.load('select box.png').convert_alpha()
            arrow = pg.image.load("arrow.png").convert_alpha()

        # At start of each new rotation of turns: checks if enemies are alive and checks if player is alive
        while self.check_enemies_alive() and int(self.fighters[player_spot].health) > 0:
            # z is a combatant. Z will loop through each element in self.fighters
            # Starts the turn
            for z in self.fighters:
                pg.event.get()
                # If the person who's turn it is is alive and enemies are alive, and player is alive: turn can be taken
                if int(z.health) > 0 and self.check_enemies_alive() and int(self.fighters[player_spot].health) > 0:
                    selected_move_name = "No Move"
                    p = 0
                    if z.isPlayer() or z.isCompanion():
                        drawArena()
                        # checks after each move if they have action points and health remaining
                        while (z.action_points > p) & (z.health > 0):
                            pg.time.delay(100)
                            # If they select to end the turn
                            # then it sets p to the total action points available per turn to end the turn
                            if selected_move_name == "Get Me Out of Here":
                                p = z.action_points
                            # input validation to ensure they select a valid move
                            while selected_move_name == "No Move":
                                print("It is " + str(z.name)[:-1] + "'s turn" + "\nRemaining Action Points: "
                                      + str((z.action_points - p)) + "\nPick a move\n1-" + z.move1.name
                                      + "\n2-" + z.move2.name + "\n3-" + z.move3.name +
                                      "\n4-" + z.move4.name + "\n5-End Turn")
                                drawPlayerStats()
                                m = 1
                                drawMoves()
                                choosing = True
                                while choosing:

                                    # set press to false
                                    press = False

                                    # each loop iterates a 10ms pause
                                    pg.time.delay(10)

                                    # exits the game
                                    for event in pg.event.get():
                                        if event.type == pg.QUIT:
                                            run = False

                                    keys = pg.key.get_pressed()

                                    if keys[pg.K_w]:
                                        if m > 3:
                                            if not press:
                                                m -= 3
                                                drawMoves()
                                                pg.time.delay(300)
                                                press = True

                                    if keys[pg.K_a]:
                                        if m != 1 and m != 4:
                                            if not press:
                                                m -= 1
                                                drawMoves()
                                                pg.time.delay(300)
                                                press = True

                                    if keys[pg.K_s]:
                                        if m < 4:
                                            if not press:
                                                m += 3
                                                drawMoves()
                                                pg.time.delay(300)
                                                press = True

                                    if keys[pg.K_d]:
                                        if m != 3 and m != 6:
                                            if not press:
                                                m += 1
                                                drawMoves()
                                                pg.time.delay(300)
                                                press = True

                                    if keys[pg.K_RETURN]:
                                        choosing = False
                                        pg.time.delay(100)

                                if m == 1:
                                    selected_move = z.move1
                                    selected_move_name = selected_move.name
                                if m == 2:
                                    selected_move = z.move2
                                    selected_move_name = selected_move.name
                                if m == 3:
                                    selected_move = z.move3
                                    selected_move_name = selected_move.name
                                if m == 4:
                                    selected_move = z.move4
                                    selected_move_name = selected_move.name
                                if m == 5:
                                    p = 0
                                    selected_move_name = "Get Me Out of Here"
                                    leave = Move("Leaving", 0, 100, 0)
                                    selected_move = leave

                            # Checks if they have enough AP to use the move and checks if they selected to end turn
                            if (selected_move.cost <= z.action_points - p) & (
                                    selected_move_name != "Get Me Out of Here"):
                                p = p + selected_move.cost
                                print("Pick a Target\n0-" + self.enemies[0].name + "\n1-" + self.enemies[
                                    1].name + "\n2-" + self.enemies[2].name)

                                d = 0
                                drawTarget()
                                pg.time.delay(500)
                                # choice has not been made yet while true
                                choosing = True
                                while choosing:

                                    # set press to false
                                    press = False

                                    # each loop iterates a 10ms pause
                                    pg.time.delay(10)

                                    # exits the game
                                    for event in pg.event.get():
                                        if event.type == pg.QUIT:
                                            run = False

                                    keys = pg.key.get_pressed()

                                    if keys[pg.K_w]:
                                        if d > 0:
                                            if not press:
                                                d -= 1
                                                drawTarget()
                                                pg.time.delay(300)
                                                press = True

                                    if keys[pg.K_s]:
                                        if d < 2:
                                            if not press:
                                                d += 1
                                                drawTarget()
                                                pg.time.delay(300)
                                                press = True

                                    if keys[pg.K_RETURN]:
                                        choosing = False
                                        pg.time.delay(100)

                                r = random.randint(0, 100)
                                selected_move_name = "No Move"
                                # Checks to see if move missed
                                if r > selected_move.accuracy:
                                    print("Move Missed!!!")
                                    drawMiss()
                                # Move hit!
                                else:
                                    self.enemies[d].health -= selected_move.power
                                    if self.enemies[d].health < 0:
                                        self.enemies[d].health = 0
                                    print("Enemy's Health is now " + str(self.enemies[d].health))
                                    drawEnemyStats()
                            # If they did not have enough AP
                            elif selected_move_name != "Get Me Out of Here":
                                print("You do not have enough Action Points :(")
                                selected_move_name = "No Move"
                    # Enemies' turn with
                    elif z.action_points != p:
                        # checks to ensure they have AP remaining
                        while z.action_points > p:
                            pg.time.delay(300)
                            r = random.randint(0, len(z.moves) - 1)
                            selected_move = z.moves[r]
                            # if they have enough AP to use the move...use the move
                            if selected_move.cost <= z.action_points - p:
                                drawEnemyAttack()
                                p = p + selected_move.cost
                                r = random.randint(0, 100)
                                # Checks to see if they missed
                                if r > selected_move.accuracy:
                                    print("They Missed!!!")
                                    drawMiss()
                                # Picks a fighter for them to attack
                                else:
                                    r = random.randint(0, 1)
                                    # Hit player
                                    if r == 0:
                                        self.fighters[player_spot].health -= selected_move.power
                                        drawPlayerHit()
                                    # Hit Companion
                                    else:
                                        self.fighters[companion_spot].health -= selected_move.power
                                        drawCompanionHit()
                                    if self.fighters[player_spot].health < 0:
                                        self.fighters[player_spot].health = 0
                                    print("Player's Health is now " + str(self.fighters[player_spot].health))
                                    if self.fighters[companion_spot].health < 0:
                                        self.fighters[companion_spot].health = 0
                                    print("Companion's Health is now " + str(self.fighters[companion_spot].health))
                            # Ends their turn
                            else:
                                p = z.action_points

    # NICKS CODE FROM SPRINT 2 -------------------------------------------------------------------------------------

    # Combat Starts by walking within enemies detection zone
    # Each action in combat will consume a set number of Action Points(AP)
    # The order of each character's turn will depend on their speed stat
    # Characters will have the option to move, attack, and/or use an item
    # Different moves will have different ranges
    # The fight ends when either the main character falls to 0 HP or all enemies are defeated
    # At the conclusion of the fight, experience points will be rewarded to the player's character and party

    # Stats will be Speed, Strength, Intelligence, Constitution

    # Class for Combat
    class Combat:
        # Constructor Method
        def __init__(self, player, companion, enemies):
            self.player = player
            self.companion = companion
            self.enemies = enemies
            if len(self.enemies) == 1:
                self.fighters = [player, companion, enemies[0]]
            if len(self.enemies) == 2:
                self.fighters = [player, companion, enemies[0], enemies[1]]
            if len(self.enemies) == 3:
                self.fighters = [player, companion, enemies[0], enemies[1], enemies[2]]

        def check_enemies_alive(self):
            for i in self.enemies:
                if i.health > 0:
                    # True = At least one enemy remains alive
                    return True
                # False = all enemies friends are dead
            return False

        def fight(self):
            battle(self)

    # Player Class
    class Player:

        # Constructor Method
        def __init__(self, name, speed, strength, intelligence, constitution, level, move1, move2, move3, move4, exp,
                     health):
            self.name = name
            self.speed = speed
            self.strength = strength
            self.intelligence = intelligence
            self.constitution = constitution
            self.level = level
            self.move1 = move1
            self.move2 = move2
            self.move3 = move3
            self.move4 = move4
            self.exp = exp
            self.health = health
            self.action_points = int(self.speed) * 3

        # Method to Write Player stats to saveFile
        def write_to_save_file(self):
            saveFile = open("saveFile.txt", "w+")
            saveFile.write("Save 1")
            saveFile.write("\n")
            saveFile.write(str(self.name))
            saveFile.write(str(self.speed))
            saveFile.write(str(self.strength))
            saveFile.write(str(self.intelligence))
            saveFile.write(str(self.constitution))
            saveFile.write(str(self.level))
            saveFile.write(self.move1.name)
            saveFile.write("\n")
            saveFile.write(self.move2.name)
            saveFile.write("\n")
            saveFile.write(self.move3.name)
            saveFile.write("\n")
            saveFile.write(self.move4.name)
            saveFile.write("\n")
            saveFile.write(str(self.exp))
            saveFile.write(str(self.health))
            saveFile.write("\n")
            saveFile.close()

        def isPlayer(self):
            return True

        def isCompanion(self):
            return False

# MAKE A CLASS FOR ITEM
    class Item:
        # Constructor Method
        def __init__(self, name, damage, healing, stamina):
            self.name = name
            self.damage = damage
            self.healing = healing
            self.stamina = stamina

        def use_item(self, war):
            if "Splash" in self.name:
                war.fighters[player_spot].health += self.healing
                war.fighters[companion_spot].health += self.healing
                for enemy in war.enemies:
                    enemy.health -= self.damage
            elif "Healing" in self.name or "Stamina" in self.name:
                war.fighters[z].health += self.healing
                war.fighters[z].action_points += self.stamina
            else:
                print("Pick a Target\n0-" + self.enemies[0].name + "\n1-" + self.enemies[
                    1].name + "\n2-" + self.enemies[2].name)

                d = 0
                drawTarget()
                pg.time.delay(500)
                # choice has not been made yet while true
                choosing = True
                while choosing:

                    # set press to false
                    press = False

                    # each loop iterates a 10ms pause
                    pg.time.delay(10)

                    # exits the game
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            run = False

                    keys = pg.key.get_pressed()

                    if keys[pg.K_w]:
                        if d > 0:
                            if not press:
                                d -= 1
                                drawTarget()
                                pg.time.delay(300)
                                press = True

                    if keys[pg.K_s]:
                        if d < 2:
                            if not press:
                                d += 1
                                drawTarget()
                                pg.time.delay(300)
                                press = True

                    if keys[pg.K_RETURN]:
                        choosing = False
                        pg.time.delay(100)
                war.enemies[d].health -= self.damage
                # redraw enemy stats
                drawEnemyStats()
            self.name = "No Item"

# MAKE A CLASS FOR INVENTORY THAT TAKES IN FIVE ITEMS AND WRITES THEM TO THE FILE ON LINES 28-32
    class Inventory:
        # Constructor Method
        def __init__(self, item1, item2, item3, item4, item5):
            self.item1 = item1
            self.item2 = item2
            self.item3 = item3
            self.item4 = item4
            self.item5 = item5

        def write_inv_to_file(self):
            saveFile = open("saveFile.txt", "a+")
            saveFile.write(str(item1.name))
            saveFile.write("\n")
            saveFile.write(str(item2.name))
            saveFile.write("\n")
            saveFile.write(str(item3.name))
            saveFile.write("\n")
            saveFile.write(str(item4.name))
            saveFile.write("\n")
            saveFile.write(str(item5.name))
            saveFile.write("\n")
            saveFile.close()

        def read_inv_from_save_file(self):
            loadFile = open("saveFile.txt", "r+")
            file = loadFile.readlines()
            item1 = file[28]
            if str("Healing Potion") in item1:
                item1 = Item("Healing Potion", 0, 50, 0)
            elif str("Splash Potion of Healing") in item1:
                item1 = Item("Splash Potion of Healing", 0, 25, 0)
            elif str("Splash Potion of Damage") in item1:
                item1 = Item("Splash Potion of Damage", 30, 0, 0)
            elif str("Tomahawk") in item1:
                item1 = Item("Tomahawk", 50, 0, 0)
            elif str("Stamina Potion") in item1:
                item1 = Item("Stamina Potion", 0, 0, 4)
            elif str("No Item") in item1:
                item1 = Item("No Item", 0, 0, 0)
            item2 = file[29]
            if str("Healing Potion") in item2:
                item2 = Item("Healing Potion", 0, 50, 0)
            elif str("Splash Potion of Healing") in item2:
                item2 = Item("Splash Potion of Healing", 0, 25, 0)
            elif str("Splash Potion of Damage") in item2:
                item2 = Item("Splash Potion of Damage", 30, 0, 0)
            elif str("Tomahawk") in item2:
                item2 = Item("Tomahawk", 50, 0, 0)
            elif str("Stamina Potion") in item2:
                item2 = Item("Stamina Potion", 0, 0, 4)
            elif str("No Item") in item2:
                item2 = Item("No Item", 0, 0, 0)
            item3 = file[30]
            if str("Healing Potion") in item3:
                item3 = Item("Healing Potion", 0, 50, 0)
            elif str("Splash Potion of Healing") in item3:
                item3 = Item("Splash Potion of Healing", 0, 25, 0)
            elif str("Splash Potion of Damage") in item3:
                item3 = Item("Splash Potion of Damage", 30, 0, 0)
            elif str("Tomahawk") in item3:
                item3 = Item("Tomahawk", 50, 0, 0)
            elif str("Stamina Potion") in item3:
                item3 = Item("Stamina Potion", 0, 0, 4)
            elif str("No Item") in item3:
                item3 = Item("No Item", 0, 0, 0)
            item4 = file[31]
            if str("Healing Potion") in item4:
                item4 = Item("Healing Potion", 0, 50, 0)
            elif str("Splash Potion of Healing") in item4:
                item4 = Item("Splash Potion of Healing", 0, 25, 0)
            elif str("Splash Potion of Damage") in item4:
                item4 = Item("Splash Potion of Damage", 30, 0, 0)
            elif str("Tomahawk") in item4:
                item4 = Item("Tomahawk", 50, 0, 0)
            elif str("Stamina Potion") in item4:
                item4 = Item("Stamina Potion", 0, 0, 4)
            elif str("No Item") in item4:
                item4 = Item("No Item", 0, 0, 0)
            item5 = file[32]
            if str("Healing Potion") in item5:
                item5 = Item("Healing Potion", 0, 50, 0)
            elif str("Splash Potion of Healing") in item5:
                item5 = Item("Splash Potion of Healing", 0, 25, 0)
            elif str("Splash Potion of Damage") in item5:
                item5 = Item("Splash Potion of Damage", 30, 0, 0)
            elif str("Tomahawk") in item5:
                item5 = Item("Tomahawk", 50, 0, 0)
            elif str("Stamina Potion") in item5:
                item5 = Item("Stamina Potion", 0, 0, 4)
            elif str("No Item") in item5:
                item5 = Item("No Item", 0, 0, 0)

            loadFile.close()
            return Inventory(item1, item2, item3, item4, item5)
# INCORPORATE ITEMS INTO FIGHT FOR IF THEY SELECT "ITEMS"

    class Enemy:
        # Constructor Method
        def __init__(self, name, speed, strength, intelligence, constitution, detection_range, level,
                     moves, health):
            self.name = name
            self.speed = speed
            self.strength = strength
            self.intelligence = intelligence
            self.constitution = constitution
            self.detection_range = detection_range
            self.level = level
            self.moves = moves
            self.health = health
            self.action_points = int(self.speed)

        def isPlayer(self):
            return False

        def isCompanion(self):
            return False

    # Move class
    class Move:
        def __init__(self, name, power, accuracy, cost):
            self.name = name
            self.power = power
            self.accuracy = accuracy
            self.cost = cost

    # Companion Class
    class Companion:
        # Constructor Method
        def __init__(self, name, speed, strength, intelligence, constitution, level, move1, move2, move3, move4,
                     health):
            self.name = name
            self.speed = speed
            self.strength = strength
            self.intelligence = intelligence
            self.constitution = constitution
            self.level = level
            self.level = level
            self.move1 = move1
            self.move2 = move2
            self.move3 = move3
            self.move4 = move4
            self.health = health
            self.action_points = int(self.speed) * 3

        # Method to Write Companion stats to saveFile
        def write_to_save_file(self):
            saveFile = open("saveFile.txt", "a+")
            saveFile.write(str(self.name))
            saveFile.write(str(self.speed))
            saveFile.write(str(self.strength))
            saveFile.write(str(self.intelligence))
            saveFile.write(str(self.constitution))
            saveFile.write(str(self.level))
            saveFile.write(self.move1.name)
            saveFile.write("\n")
            saveFile.write(self.move2.name)
            saveFile.write("\n")
            saveFile.write(self.move3.name)
            saveFile.write("\n")
            saveFile.write(self.move4.name)
            saveFile.write("\n")
            saveFile.write(str(self.health))
            saveFile.write("\n")
            saveFile.write("---")
            saveFile.write("\n")
            saveFile.write("---")
            saveFile.write("\n")
            saveFile.close()

        def isPlayer(self):
            return False

        def isCompanion(self):
            return True

    def player_read_from_save_file():
        loadFile = open("saveFile.txt", "r+")
        file = loadFile.readlines()
        name = file[1]
        speed = file[2]
        strength = file[3]
        intelligence = file[4]
        constitution = file[5]
        level = file[6]
        move1 = file[7]
        print(move1)
        if str("Bone Breaker") in move1:
            move1 = Move("Bone Breaker", 50, 95, 4)
        elif str("Axe Throw") in move1:
            move1 = Move("Axe Throw", 60, 80, 6)
        elif str("Sword Slash") in move1:
            move1 = Move("Sword Slash", 40, 95, 3)
        elif str("Throwing Knife") in move1:
            move1 = Move("Throwing Knife", 15, 90, 1)
        elif str("Ranger Shot") in move1:
            move1 = Move("Ranger Shot", 40, 90, 3)
        elif str("Bow Melee") in move1:
            move1 = Move("Bow Melee", 10, 99, 2)
        elif str("No Move") in move1:
            move1 = Move("No Move", 0, 0, 0)
        move2 = file[8]
        if str("Bone Breaker") in move2:
            move2 = Move("Bone Breaker", 50, 95, 4)
        elif str("Axe Throw") in move2:
            move2 = Move("Axe Throw", 60, 80, 6)
        elif str("Sword Slash") in move2:
            move2 = Move("Sword Slash", 40, 95, 3)
        elif str("Throwing Knife") in move2:
            move2 = Move("Throwing Knife", 15, 90, 1)
        elif str("Ranger Shot") in move2:
            move2 = Move("Ranger Shot", 40, 90, 3)
        elif str("Bow Melee") in move2:
            move2 = Move("Bow Melee", 10, 99, 2)
        elif str("No Move") in move2:
            move2 = Move("No Move", 0, 0, 0)
        move3 = file[9]
        if str("Bone Breaker") in move3:
            move3 = Move("Bone Breaker", 50, 95, 4)
        elif str("Axe Throw") in move3:
            move3 = Move("Axe Throw", 60, 80, 6)
        elif str("Sword Slash") in move3:
            move3 = Move("Sword Slash", 40, 95, 3)
        elif str("Throwing Knife") in move3:
            move3 = Move("Throwing Knife", 15, 90, 1)
        elif str("Ranger Shot") in move3:
            move3 = Move("Ranger Shot", 40, 90, 3)
        elif str("Bow Melee") in move3:
            move3 = Move("Bow Melee", 10, 99, 2)
        elif str("No Move") in move3:
            move3 = Move("No Move", 0, 0, 0)
        move4 = file[10]
        if str("Bone Breaker") in move4:
            move4 = Move("Bone Breaker", 50, 95, 4)
        elif str("Axe Throw") in move4:
            move4 = Move("Axe Throw", 60, 80, 6)
        elif str("Sword Slash") in move4:
            move4 = Move("Sword Slash", 40, 95, 3)
        elif str("Throwing Knife") in move4:
            move4 = Move("Throwing Knife", 15, 90, 1)
        elif str("Ranger Shot") in move4:
            move4 = Move("Ranger Shot", 40, 90, 3)
        elif str("Bow Melee") in move4:
            move4 = Move("Bow Melee", 10, 99, 2)
        elif str("Debug") in move4:
            move4 = Move("Debug", 10000, 100, 0)
        elif str("No Move") in move4:
            move4 = Move("No Move", 0, 0, 0)
        exp = file[11]
        health = int(file[12])
        loadFile.close()
        return Player(name, speed, strength, intelligence, constitution, level, move1, move2, move3, move4, exp, health)

    def companion_read_from_save_file():
        loadFile = open("saveFile.txt", "r+")
        file = loadFile.readlines()
        name = file[13]
        speed = file[14]
        strength = file[15]
        intelligence = file[16]
        constitution = file[17]
        level = file[18]
        move1 = file[19]
        if str("Bone Breaker") in move1:
            move1 = Move("Bone Breaker", 50, 95, 4)
        elif str("Axe Throw") in move1:
            move1 = Move("Axe Throw", 60, 80, 6)
        elif str("Sword Slash") in move1:
            move1 = Move("Sword Slash", 40, 95, 3)
        elif str("Throwing Knife") in move1:
            move1 = Move("Throwing Knife", 15, 90, 1)
        elif str("Ranger Shot") in move1:
            move1 = Move("Ranger Shot", 40, 90, 3)
        elif str("Bow Melee") in move1:
            move1 = Move("Bow Melee", 10, 99, 2)
        elif str("No Move") in move1:
            move1 = Move("No Move", 0, 0, 0)
        move2 = file[20]
        if str("Bone Breaker") in move2:
            move2 = Move("Bone Breaker", 50, 95, 4)
        elif str("Axe Throw") in move2:
            move2 = Move("Axe Throw", 60, 80, 6)
        elif str("Sword Slash") in move2:
            move2 = Move("Sword Slash", 40, 95, 3)
        elif str("Throwing Knife") in move2:
            move2 = Move("Throwing Knife", 15, 90, 1)
        elif str("Ranger Shot") in move2:
            move2 = Move("Ranger Shot", 40, 90, 3)
        elif str("Bow Melee") in move2:
            move2 = Move("Bow Melee", 10, 99, 2)
        elif str("No Move") in move2:
            move2 = Move("No Move", 0, 0, 0)
        move3 = file[21]
        if str("Bone Breaker") in move3:
            move3 = Move("Bone Breaker", 50, 95, 4)
        elif str("Axe Throw") in move3:
            move3 = Move("Axe Throw", 60, 80, 6)
        elif str("Sword Slash") in move3:
            move3 = Move("Sword Slash", 40, 95, 3)
        elif str("Throwing Knife") in move3:
            move3 = Move("Throwing Knife", 15, 90, 1)
        elif str("Ranger Shot") in move3:
            move3 = Move("Ranger Shot", 40, 90, 3)
        elif str("Bow Melee") in move3:
            move3 = Move("Bow Melee", 10, 99, 2)
        elif str("No Move") in move3:
            move3 = Move("No Move", 0, 0, 0)
        move4 = file[22]
        if str("Bone Breaker") in move4:
            move4 = Move("Bone Breaker", 50, 95, 4)
        elif str("Axe Throw") in move4:
            move4 = Move("Axe Throw", 60, 80, 6)
        elif str("Sword Slash") in move4:
            move4 = Move("Sword Slash", 40, 95, 3)
        elif str("Throwing Knife") in move4:
            move4 = Move("Throwing Knife", 15, 90, 1)
        elif str("Ranger Shot") in move4:
            move4 = Move("Ranger Shot", 40, 90, 3)
        elif str("Bow Melee") in move4:
            move4 = Move("Bow Melee", 10, 99, 2)
        elif str("Debug") in move4:
            move4 = Move("Debug", 10000, 100, 0)
        elif str("No Move") in move4:
            move4 = Move("No Move", 0, 0, 0)
        health = int(file[23])
        loadFile.close()
        return Companion(name, speed, strength, intelligence, constitution, level, move1, move2, move3, move4, health)

    # Making Player's moves
    BoneBreaker = Move("Bone Breaker", 50, 95, 4)
    AxeThrow = Move("Axe Throw", 60, 80, 6)

    # Placeholder Move
    NoMove = Move("No Move", 0, 0, 0)

    # Making Companion Moves
    SwordSlash = Move("Sword Slash", 40, 95, 3)
    ThrowingKnife = Move("Throwing Knife", 15, 90, 1)

    # Skeleton Archer's Move Set
    RangerShot = Move("Ranger Shot", 40, 90, 3)
    BowPunch = Move("Bow Melee", 10, 99, 2)
    Skeleton_Archer_Move_Set = [RangerShot, BowPunch]

    # Skeleton Archer
    Skeleton_Archer1 = Enemy("Skeleton Archer", 5, 7, 4, 3, 10, 10, Skeleton_Archer_Move_Set, 100)
    Skeleton_Archer2 = Enemy("Skeleton Archer", 5, 7, 4, 3, 10, 10, Skeleton_Archer_Move_Set, 100)
    Skeleton_Archer3 = Enemy("Skeleton Archer", 5, 7, 4, 3, 10, 10, Skeleton_Archer_Move_Set, 100)

    # END OF NICKS CODE-----------------------------------------------------------------------------------------------

    class OverworldEnemy():

        # CONSTRUCTOR
        # ox original x position
        # oy original y position
        # x current x position
        # y current y position
        # type string that determines type of enemy
        def __init__(self, x, y, type):
            self.ox = x
            self.oy = y
            self.x = self.ox
            self.y = self.oy
            self.type = type
            if type == "skeleton":
                self.image = pg.image.load('skeleton.png').convert_alpha()

        # called at the end of the fight, teleports enemy off screen
        def defeated(self):
            self.x = 9000

        # check for collision with player to start fight
        def checkFight(self, x, y):
            if y == self.y:
                if (x > (self.x - 60)) & (x < (self.x + 60)):
                    # enter fight
                    fight1.fight()
                    self.defeated()

            elif x == self.x:
                if (y > (self.y - 60)) & (y < (self.y + 60)):
                    # enter fight
                    fight1.fight()
                    self.defeated()

        # semi-random movement around the overworld map
        def move(self):
            r = random.randint(1, 5)

            # move right
            if r == 1 and (self.x < (self.ox + 128)):
                return "right"
            elif r == 1:
                return "none"
            # move left
            if r == 2 and (self.x > (self.ox - 128)):
                return "left"
            elif r == 2:
                return "none"

            # move down
            if r == 3 and (self.y < (self.oy + 128)):
                return "down"
            elif r == 3:
                return "none"

            # move up
            if r == 4 and (self.y > (self.oy - 128)):
                return "up"
            elif r == 4:
                return "none"

            if r == 5:
                return "none"

    # Making a Player Instance
    player1 = player_read_from_save_file()
    # Making a Companion Instance
    comp = companion_read_from_save_file()
    # Saving Player and Companion
    player1.write_to_save_file()
    comp.write_to_save_file()
    enemies1 = [Skeleton_Archer1, Skeleton_Archer2, Skeleton_Archer3]
    fighters1 = [player1, comp, Skeleton_Archer1, Skeleton_Archer2, Skeleton_Archer3]
    fight1 = Combat(player1, comp, enemies1)

    # text
    myFont = pg.font.Font('MANDATOR.ttf', 32)
    smallFont = pg.font.Font('MANDATOR.ttf', 24)
    nameText = myFont.render(playerName, False, (250, 250, 250))
    companionText = myFont.render(comp.name[:-1], False, (250, 250, 250))

    win = pg.display.set_mode((1280, 720))
    pg.display.set_caption("Project Bubbas")
    x = 128
    y = 56
    x2 = x - 64
    y2 = y
    ex = 960
    ey = 320
    width = 64
    height = 64
    vel = 5
    wait = 0

    # integer that defines which sprite is used
    charOr = 0

    # initialize player direction and enemy direction
    pDir = "none"
    eDir = "none"

    # character movement frames - resets to 0 after 64
    pMove = 0

    # enemy movement frames - resets to 0 after 64
    eMove = 0

    # the press variable determines if a key has been pressed in this iteration of the loop
    press = False

    # load images for player directions
    playerDown = pg.transform.scale(pg.image.load('elf.png').convert_alpha(), (64, 72))
    playerUp = pg.transform.scale(pg.image.load('elf behind.png').convert_alpha(), (64, 72))
    playerLeft = pg.transform.scale(pg.image.load('elf side.png').convert_alpha(), (64, 72))
    playerRight = pg.transform.scale(pg.image.load('elf mage right.png').convert_alpha(), (64, 72))

    # load images for companion directions
    compDown = pg.transform.scale(pg.image.load('elf knight down.png').convert_alpha(), (64, 72))
    compUp = pg.transform.scale(pg.image.load('elf knight up.png').convert_alpha(), (64, 72))
    compLeft = pg.transform.scale(pg.image.load('elf knight left.png').convert_alpha(), (64, 72))
    compRight = pg.transform.scale(pg.image.load('elf knight right.png').convert_alpha(), (64, 72))

    # load images, initialize char1 to down
    char1 = playerDown
    char2 = compDown
    room1 = pg.image.load('room.jpg').convert()
    dungeonArena = pg.image.load('dungeon arena.jpg').convert()
    enemy1 = pg.image.load('skeleton.png').convert_alpha()

    # create necessary objects
    skeletonArcher = OverworldEnemy(ex, ey, "skeleton")

    # text to screen
    font = pg.font.SysFont(None, 25)

    def drawPlayArea():

        # draw area
        win.blit(room1, (0, 0))
        # check for collision
        skeletonArcher.checkFight(x, y)
        # draw characters
        win.blit(enemy1, (skeletonArcher.x, skeletonArcher.y))
        if y2 < y:
            win.blit(char2, (x2, y2))
            win.blit(char1, (x, y))
        else:
            win.blit(char1, (x, y))
            win.blit(char2, (x2, y2))

        # draw bar
        pg.draw.rect(win, (2, 2, 2), (0, 512, 1280, 208))
        win.blit(playerDown, (20, 520))
        win.blit(compDown, (300, 520))
        win.blit(nameText, (100, 530))
        win.blit(companionText, (380, 530))

        pg.time.delay(3)

        # update display
        pg.display.update()

    run = True
    while run:

        # each loop iterates a 1ms pause
        pg.time.delay(1)

        # exits the game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            if not press:
                char1 = playerUp
                # keeps player in bounds
                if y > 56:
                    pDir = "up"
                    # xt and yt are temporary variables to control companion's movement
                    xt = x
                    yt = y
                    press = True

        if keys[pg.K_a]:
            if not press:
                char1 = playerLeft
                if x > 64:
                    pDir = "left"
                    yt = y
                    xt = x
                    press = True

        if keys[pg.K_s]:
            if not press:
                char1 = playerDown
                if y < 440:
                    pDir = "down"
                    xt = x
                    yt = y
                    press = True

        if keys[pg.K_d]:
            if not press:
                char1 = playerRight
                if x < 1152:
                    pDir = "right"
                    yt = y
                    xt = x
                    press = True

        # calculation to determine if enemies should move
        if eDir == "none":
            wait += 1
            waitTime = random.randint(250, 1500)
            if wait >= waitTime:
                eDir = skeletonArcher.move()
                if eDir == "none":
                    wait = 0

        # initiate movement animations
        if pDir != "none" or eDir != "none":

            # check to see if player movement is completed
            if pMove >= 64:
                pDir = "none"
                press = False
                pg.time.delay(50)
                pMove = 0

            if eMove >= 64:
                eDir = "none"
                eMove = 0
                wait = 0

            # if player moves right
            if pDir == "right":
                if x2 == xt:
                    # if the player and companion are at same Y coordinate, this if statement checks if companion is
                    # above or below the player
                    if y2 < yt:
                        y2 += 1
                        char2 = compDown
                    else:
                        y2 -= 1
                        char2 = compUp
                    # if player and companion are at two different x coordinates, test for left or right
                elif x2 > xt:
                    x2 -= 1
                    char2 = compLeft
                else:
                    x2 += 1
                    char2 = compRight
                    # player's vertical position goes 8 up, 8 times to reach one 64 pixel block
                x += 1
                pMove += 1

            # if player moves left
            if pDir == "left":
                # if statement checks to see if player and companion are at same X coordinate
                if x2 == xt:
                    # if the player and companion are at same Y coordinate, this if statement checks if
                    # companion is above or below the player
                    if y2 < yt:
                        y2 += 1
                        char2 = compDown
                    else:
                        y2 -= 1
                        char2 = compUp
                # if player and companion are at two different x coordinates, test for left or right
                elif x2 > xt:
                    x2 -= 1
                    char2 = compLeft
                else:
                    x2 += 1
                    char2 = compRight
                # player's vertical position goes 8 up, 8 times to reach one 64 pixel block
                x -= 1
                pMove += 1

            # if player moves up
            if pDir == "up":
                # if statement checks to see if player and companion are at same Y coordinate
                if y2 == yt:
                    # if the player and companion are at same Y coordinate, this if statement checks if companion is
                    # to the left or right of the player
                    if x2 < xt:
                        x2 += 1
                        char2 = compRight
                    else:
                        x2 -= 1
                        char2 = compLeft
                # if player and companion are at two different y coordinates, test for above or below
                elif y2 > yt:
                    y2 -= 1
                    char2 = compUp
                else:
                    y2 += 1
                    char2 = compDown
                # player's vertical position goes 8 up, 8 times to reach one 64 pixel block
                y -= 1
                pMove += 1

            # if player moves down
            if pDir == "down":
                # if statement checks to see if player and companion are at same Y coordinate
                if y2 == yt:
                    # if the player and companion are at same Y coordinate, this if statement checks if companion is
                    # to the left or right of the player
                    if x2 < xt:
                        x2 += 1
                        char2 = compRight
                    else:
                        x2 -= 1
                        char2 = compLeft
                # if player and companion are at two different y coordinates, test for above or below
                elif y2 > yt:
                    y2 -= 1
                    char2 = compUp
                else:
                    y2 += 1
                    char2 = compDown
                # player's vertical position goes 8 up, 8 times to reach one 64 pixel block
                y += 1
                pMove += 1

            if eDir == "right":
                skeletonArcher.x += 1
                eMove += 1
                print(f'{skeletonArcher.x:>5f} {skeletonArcher.ox:>10f}')

            if eDir == "left":
                skeletonArcher.x -= 1
                eMove += 1

            if eDir == "up":
                skeletonArcher.y -= 1
                eMove += 1

            if eDir == "down":
                skeletonArcher.y += 1
                eMove += 1

        drawPlayArea()

    pg.quit()


def dennis():
    # making the window
    window = Tk()
    window.title("Character Creation")
    window.geometry('1920x1080')

    plyrName = ""
    gender = "male"
    plyrRace = ""
    plyrClass = ""
    classBio = ""

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
        saveFile.write(str(txtName))
        saveFile.write("\n")
        saveFile.write(str(4))
        saveFile.write("\n")
        saveFile.write(str(5))
        saveFile.write("\n")
        saveFile.write(str(6))
        saveFile.write("\n")
        saveFile.write(str(7))
        saveFile.write("\n")
        saveFile.write(str(10))
        saveFile.write("\n")
        saveFile.write("Bone Breaker")
        saveFile.write("\n")
        saveFile.write("Axe Throw")
        saveFile.write("\n")
        saveFile.write("No Move")
        saveFile.write("\n")
        saveFile.write("No Move")
        saveFile.write("\n")
        saveFile.write(str(50))
        saveFile.write("\n")
        saveFile.write(str(170))
        saveFile.write("\n")
        saveFile.write(str("Nick"))
        saveFile.write("\n")
        saveFile.write(str(1))
        saveFile.write("\n")
        saveFile.write(str(2))
        saveFile.write("\n")
        saveFile.write(str(3))
        saveFile.write("\n")
        saveFile.write(str(6))
        saveFile.write("\n")
        saveFile.write(str(10))
        saveFile.write("\n")
        saveFile.write("Sword Slash")
        saveFile.write("\n")
        saveFile.write("Throwing Knife")
        saveFile.write("\n")
        saveFile.write("No Move")
        saveFile.write("\n")
        saveFile.write("No Move")
        saveFile.write("\n")
        saveFile.write(str(160))
        saveFile.close()
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


# New Game Command
def new_game():
    # insert code to move to character selection screen

    mainMenu.destroy()
    dennis()


# Continue Game Command
def cont_game():
    loadFile = open("saveFile.txt", "r+")
    file = loadFile.readlines()
    playerName = file[1][:-1]
    messagebox.showinfo("Hello There", "Welcome back, " + playerName + "\nLoading you back into the game now.")
    pyGame(playerName)


# Code for the close window command attached to the exit Button
def close_window():
    mainMenu.destroy()


# Create Buttons for Main Menu
continue_game = tkinter.Button(mainMenu, text="Continue", command=cont_game, padx=75, pady=30)
new_game = tkinter.Button(mainMenu, text="New Game", padx=75, pady=30, command=new_game)
optionsButton = tkinter.Button(mainMenu, text="Options", padx=75, pady=30)
exitButton = tkinter.Button(mainMenu, text="Exit Game", command=close_window, padx=75, pady=30)

# Place Widgets
continue_game.place(x=550, y=300)
new_game.place(x=550, y=400)
optionsButton.place(x=550, y=500)
exitButton.place(x=550, y=600)

mainMenu.mainloop()