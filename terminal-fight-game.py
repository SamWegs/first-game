import random

class Character:
    
    def __init__(self, name, classification, level = 1):
        self.name = name
        self.classification = classification
        self.level = level
        self.strength = level * 5
        self.hitpoints = 100 + level * 10
        self.alive = True

    def __repr__(self):
        return f"{self.name}, is a level {self.level}. He has {self.hitpoints} HP. His strength is {self.strength}."
    
    def attack(self):
        hit_dice = random.randint(1,6)
        damage_dealt = 0
        if hit_dice == 1:
            damage_dealt = 0 * self.strength
        elif hit_dice == 2 or hit_dice == 3:
            damage_dealt = 1 * self.strength
        elif hit_dice == 4 or hit_dice == 5:
            damage_dealt = 2 * self.strength
        else:
            damage_dealt = 3 * self.strength
        return damage_dealt
    
    def shout_buff(self):
        self.strength += 10
        print(f"{self.name} lets out a roar of anger increasing his strength to {self.strength}")       
        
    def take_damage(self, hp_lost):
        if (self.hitpoints - hp_lost) <= 0:
            self.hitpoints -= hp_lost
            self.alive = False
            return print(f"{self.name} takes a critical blow of {hp_lost} damage and has died on the battlefield!")
        else:
            self.hitpoints -= hp_lost
            print(f"{self.name} has been attacked for {hp_lost} damage. He has {self.hitpoints} HP left!")
        return self.hitpoints

        
class Enemy:

    def __init__(self, name, classification, level = 1):
        self.name = name
        self.classification = classification
        self.level = level
        self.e_hitpoints = 100 + level * 10
        self.strength = level * 5
        self.e_alive = True

    def __repr__(self):
        return f"{self.name} is a level {self.level}. It currently has {self.e_hitpoints} HP. Its strength is {self.strength}!"
    
    def e_attack(self):
        e_hit_dice = random.randint(1,6)
        damage_dealt = 0
        if e_hit_dice == 1:
            damage_dealt = 0 * self.strength
        elif e_hit_dice == 2 or e_hit_dice == 3:
            damage_dealt = 1 * self.strength
        elif e_hit_dice == 4 or e_hit_dice == 5:
            damage_dealt = 2 * self.strength
        else:
            damage_dealt = 3 * self.strength
        return damage_dealt
    
    def e_shout_buff(self):
        self.strength += 10
        print(f"{self.name} lets out a roar of anger increasing its strength to {self.strength}")
        
    def e_take_damage(self, hp_lost):
        if (self.e_hitpoints - hp_lost) <= 0:
            self.e_hitpoints -= hp_lost
            self.e_alive = False
            return print(f"{self.name} takes {hp_lost} damage and has been defeated on the battlefield!")
        else:
            self.e_hitpoints -= hp_lost
            print(f"{self.name} has been attacked for {hp_lost} damage. It is now at {self.e_hitpoints} HP!")
        return self.e_hitpoints

# Define instances of characters and enemies that can be selected later
warrior = Character("Warrior", "Warrior", 3)
rogue = Character("Rogue", "Rogue", 5)
gnoll = Enemy("Gnoll", "Humanoid", 3)
treant = Enemy("Treant", "Spirit", 5)

print(warrior)
print(rogue)
print(gnoll)
print(treant)

# Random select the ability of the enemy CPU
def computer_ability():
    return random.randint(1, 6)

# Prompts user input to select 1 of the 2 Character instances established
def player_select():
    player = ''
    choice = input(f"What hero do you select?! 'warrior' or 'rogue' ")
    if choice == 'warrior':
        player = warrior
    elif choice == 'rogue':
        player = rogue
    else:
        pass
    return player

# Prompts the user to select 1 of the 2 Enemy instances established
def computer_select():
    computer = ''
    choice = input(f"What foe do you select?! 'gnoll' or 'treant' ")
    if choice == 'gnoll':
        computer = gnoll
    elif choice == 'treant':
        computer = treant
    else:
        pass
    return computer

# Prompts user to select a character action. Enemy then randomly uses an action before returning loop. Ends on 0 health.
def combat(player, computer):

    while player.alive == True and computer.e_alive == True:
        
        choice = input(f"What is the {player.name}'s move? 'attack' or 'shout' ('exit' to escape the game)? ")
        if choice == 'exit':
            break
        elif choice == 'attack':
            computer.e_take_damage(player.attack())
            if computer.e_alive == True:
                if computer_ability() in range(1, 4):
                    player.take_damage(computer.e_attack())
                else: 
                    computer.e_shout_buff()
            else:
                break
        elif choice == 'shout':
            player.shout_buff()
            if computer.e_alive == True:
                if computer_ability() in range(1, 4):
                    player.take_damage(computer.e_attack())
                else: 
                    computer.e_shout_buff()
            else:
                break
        else:
            break


player = player_select()
computer = computer_select()
combat(player, computer)
    
        