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
    def __init__(self, player, companion, enemies, fighters):
        self.player = player
        self.companion = companion
        self.enemies = enemies
        self.fighters = fighters

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

        # Orders Fighters by Speed
        for i in range(n):
            for j in range(0, n - i - 1):
                if int(self.fighters[j].speed) > int(self.fighters[j+1].speed):
                    self.fighters[j], self.fighters[j+1] = self.fighters[j+1], self.fighters[j]

        while int(self.player.health) > 0 and self.check_enemies_alive(self.enemies):
            for z in self.fighters:
                if z.isPlayer:
                    while int(z.action_points) > p:
                        print("Pick a move\n1-" + z.move_list[0].name + "\n2-" + z.move_list[1].name)
                        m = int(input())
                        if m == 1:
                            selected_move = z.move_list[0]
                        if m == 2:
                            selected_move = z.move_list[1]
                        if selected_move.cost <= z.action_points - p:
                            p = p + selected_move.cost
                            print("Pick a Target\n0-" + self.enemies[0].name + "\n1-" + self.enemies[1].name + "\n2-" + self.enemies[2].name)
                            d = int(input())
                            r = random.randint(0, 100)
                            if r > selected_move.accuracy:
                                print("Move Missed!!!")
                            else:
                                self.enemies[d].health -= selected_move.power
                                if self.enemies[d].health < 0:
                                    self.enemies[d].health = 0
                                print("Enemy's Health is now" + self.enemies[d].health)

                else:
                    while z.action_points > p:
                        r = random.randint(0, 1)
                        selected_move = z.move_list[r]
                        if selected_move.cost <= z.action_points - p:
                            p = p + selected_move.cost
                            r = random.randint(0, 100)
                            if r > selected_move.accuracy:
                                print("They Missed!!!")
                            else:
                                r = random.randint(0, 1)
                                if r == 0:
                                    self.player.health -= selected_move.power
                                else:
                                    self.companion.health -= selected_move.power

                                if self.player.health < 0:
                                    self.player.health = 0
                                    print("Player's Health is now" + self.player.health)
                                if self.companion.health < 0:
                                    self.companion.health < 0
                                    print("Companion's Health is now" + self.Companion.health)


# Player Class
class Player:

    # Constructor Method
    def __init__(self):
        self.read_from_save_file()
        self.action_points = int(self.speed) * 3

    # Method to Write Player stats to saveFile
    def write_to_save_file(self):
        from json import dumps
        x = {
            "name":self.name,
            "speed":self.speed,
            "strength":self.strength,
            "intelligence":self.intelligence,
            "constitution":self.constitution,
            "level":self.level,
            "move_list":self.move_list,
            "exp":self.exp,
            "health":self.health
        }
        saveFile = open("saveFile.txt", "w+")
        saveFile.write(dumps(x))
        saveFile.close()

    # Method to Read Player stats from saveFile
    def read_from_save_file(self):
        from json import loads
        loadFile = open("saveFile.txt", "r+")
        y = loadFile.read()
        loadFile.close()
        y = loads(y)
        self.name = y["name"]
        self.speed = y["speed"]
        self.strength = y["strength"]
        self.intelligence = y["intelligence"]
        self.constitution = y["constitution"]
        self.level = y["level"]
        self.move_list = y["move_list"]
        self.exp = y["exp"]
        self.health = y["health"]

    def isPlayer(self):
        return True

class Enemy:
    # Constructor Method
    def __init__(self, name, speed, strength, intelligence, constitution, detection_range, level, move_list, health):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.constitution = constitution
        self.detection_range = detection_range
        self.level = level
        self.move_list = move_list
        self.health = health
        self.action_points = int(self.speed) * 3

    def isPlayer(self):
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
    def __init__(self):
        self.read_from_save_file()
        self.action_points = int(self.speed) * 3

    # Method to Write Companion stats to saveFile
    def write_to_save_file(self):
        from json import dumps
        x = {
            "name": self.name,
            "speed": self.speed,
            "strength": self.strength,
            "intelligence": self.intelligence,
            "constitution": self.constitution,
            "level": self.level,
            "move_list": self.move_list,
            "health": self.health
        }
        saveFile = open("saveFile.txt", "a+")
        saveFile.write(dumps(x))
        saveFile.close()

    # Method to Read Companion stats from saveFile
    def read_from_save_file(self):
        from json import loads
        loadFile = open("saveFile.txt", "r+")
        y = loadFile.read()
        y = loadFile.read()
        loadFile.close()
        y = loads(y)
        self.name = y["name"]
        self.speed = y["speed"]
        self.strength = y["strength"]
        self.intelligence = y["intelligence"]
        self.constitution = y["constitution"]
        self.level = y["level"]
        self.move_list = y["move_list"]
        self.health = y["health"]

    def isPlayer(self):
        return True

# Creating list for the loadFile
lf = open("saveFile.txt", "r+")
file1 = lf.readlines()


# Making Player's move list
BoneBreaker = Move("Bone Breaker", 50, 95, 4)
AxeThrow = Move("Axe Throw", 60, 80, 6)
player_move_list = [BoneBreaker, AxeThrow]

# Making a Player Instance
player1 = Player()
player1.write_to_save_file()



# Making Companion Move Set
SwordSlash = Move("Sword Slash", 40, 95, 3)
ThrowingKnife = Move("Throwing Knife", 15, 90, 1)
Companion_Move_Set = [SwordSlash, ThrowingKnife]

# Making a Companion Instance
comp = Companion()
comp.write_to_save_file()


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

fight1 = Combat(player1, comp, enemies1, fighters1)
fight1.fight(fighters1)