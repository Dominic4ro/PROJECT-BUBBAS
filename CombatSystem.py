import random
#20x8 dungeon room

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
        a = len(self.enemies)
        n = len(self.fighters)
        i = 0
        p = 0
        m = 0
        q = 0
        player_spot = 0
        companion_spot =0

        # Orders Fighters by Speed
        for i in range(n):
            for j in range(0, n - i - 1):
                if int(self.fighters[j].speed) < int(self.fighters[j+1].speed):
                    self.fighters[j], self.fighters[j+1] = self.fighters[j+1], self.fighters[j]
        while q < len(self.fighters):
            if self.fighters[q].isPlayer():
                player_spot = q
            if self.fighters[q].isCompanion():
                companion_spot = q
            q += 1
        print(self.fighters)
        while self.check_enemies_alive() and int(self.fighters[player_spot].health) > 0:
            for z in self.fighters:
                print(z.health)
                print(self.check_enemies_alive())
                print(self.fighters[player_spot].health)
                if int(z.health) > 0 and self.check_enemies_alive() and int(self.fighters[player_spot].health) > 0:
                    selected_move_name = "No Move"
                    p = 0
                    if z.isPlayer() or z.isCompanion():
                        while (z.action_points > p) & (z.health > 0):
                            if selected_move_name == "Get Me Out of Here":
                                p = z.action_points
                            while selected_move_name == "No Move":
                                print("It is " + str(z.name) + "'s turn" + "\nRemaining Action Points: "
                                      + str((z.action_points - p)) + "\nPick a move\n1-" + z.move1.name
                                      + "\n2-" + z.move2.name + "\n3-" + z.move3.name +
                                      "\n4-" + z.move4.name + "\n5-End Turn")
                                m = int(input())
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
                            if (selected_move.cost <= z.action_points - p) & (selected_move_name != "Get Me Out of Here"):
                                p = p + selected_move.cost
                                print("Pick a Target\n0-" + self.enemies[0].name + "\n1-" + self.enemies[1].name + "\n2-" + self.enemies[2].name)
                                d = int(input())
                                r = random.randint(0, 100)
                                selected_move_name = "No Move"
                                if r > selected_move.accuracy:
                                    print("Move Missed!!!")
                                else:
                                    self.enemies[d].health -= selected_move.power
                                    if self.enemies[d].health < 0:
                                        self.enemies[d].health = 0
                                    print("Enemy's Health is now " + str(self.enemies[d].health))
                            elif selected_move_name != "Get Me Out of Here":
                                print("You do not have enough Action Points :(")
                                selected_move_name = "No Move"
                    elif z.action_points != p:
                        while z.action_points > p:
                            r = random.randint(0, len(z.moves) - 1)
                            selected_move = z.moves[r]
                            if selected_move.cost <= z.action_points - p:
                                p = p + selected_move.cost
                                r = random.randint(0, 100)
                                if r > selected_move.accuracy:
                                    print("They Missed!!!")
                                else:
                                    r = random.randint(0, 1)
                                    if r == 0:
                                        self.fighters[player_spot].health -= selected_move.power
                                    else:
                                        self.fighters[companion_spot].health -= selected_move.power

                                    if self.fighters[player_spot].health < 0:
                                        self.fighters[player_spot].health = 0
                                    print("Player's Health is now" + str(self.fighters[player_spot].health))
                                    if self.fighters[companion_spot].health < 0:
                                        self.fighters[companion_spot].health = 0
                                    print("Companion's Health is now" + str(self.fighters[companion_spot].health))
                            else:
                                p = z.action_points

# Player Class
class Player:

    # Constructor Method
    def __init__(self, name, speed, strength, intelligence, constitution, level, move1, move2, move3, move4, exp, health):
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
    def __init__(self, name, speed, strength, intelligence, constitution, level, move1, move2, move3, move4, health):
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
    elif str("No Move") in move4:
        move4 = Move("No Move", 0, 0, 0)
    exp = file[11]
    health = int(file[12])
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
    print(len(move1))
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
    elif str("No Move") in move4:
        move4 = Move("No Move", 0, 0, 0)
    health = int(file[23])
    loadFile.close()
    return Companion(name, speed, strength, intelligence, constitution,
                     level, move1, move2, move3, move4, health)


# Making Player's moves
BoneBreaker = Move("Bone Breaker", 50, 95, 4)
AxeThrow = Move("Axe Throw", 60, 80, 6)

# Placeholder Move
NoMove = Move("No Move", 0, 0, 0)


# Making a Player Instance
player1 = player_read_from_save_file()
# Making a Companion Instance
comp = companion_read_from_save_file()
# Saving Player and Companion
player1.write_to_save_file()
comp.write_to_save_file()
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

enemies1 = [Skeleton_Archer1, Skeleton_Archer2, Skeleton_Archer3]
fighters1 = [player1, comp, Skeleton_Archer1, Skeleton_Archer2, Skeleton_Archer3]

fight1 = Combat(player1, comp, enemies1)
fight1.fight()