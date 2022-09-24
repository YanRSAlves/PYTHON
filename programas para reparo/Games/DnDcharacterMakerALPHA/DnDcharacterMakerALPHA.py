#!/usr/bin/python
# DnDcharacterMakerALPHA.py
# Saturday, September 1, 2001
# Rob Andrews
# 
# This is the first stage of development for a character generator 
# compatible with Dungeons & Dragons 3rd Edition. It should take 
# some time to get it all right, because I'm aiming for 100% 
# compatibility. This process should follow the procedure described 
# in the 3rd Edition Player's Handbook.
# 
# At some point in the process, I want to add a GUI and a number of 
# user options for character generation. I have in mind another 
# fully-OOP way of doing all this, too. However, it's really 
# involved, and it will take me some time to work out some of the 
# details.
#
# I've just made a little time for a second session working on this.
# Anyone who can provide a little input as this progresses will be
# doing a good deed. 4;->
#
###################################################################

# Import any needed modules.
import random

# Create the character dictionary.
character={}

# Name Character.
character['name'] = raw_input("What is the character's name? ")

# Create the classes list.
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard']

# Assign a class randomly from classes.
character['class'] = random.choice(classes)

# Create the races list.
races = ['Human', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling']

# Assign a race randomly from races.
character['race'] = random.choice(races)

# Create the abilities list.
abilities = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

# Add abilities and scores to character.
def generateAbilityScores():
    for n in abilities:
        ability = n
        abilityScore = random.randrange(3, 18)
        character[ability] = abilityScore
        print '%s --> %d\n' % (ability, abilityScore)
        if abilityScore < 13:
            abilityIncrease = raw_input("This ability score is below 13, so you may increase its value if you wish.\nEnter a number 0 through 5 to increase this skill by that amount: ")
            if abilityIncrease not in ['0', '1', '2', '3', '4', '5']:
                abilityIncrease = 0
                print "You did not select an increase between 0 and 5. No changes made."
            abilityIncrease = int(abilityIncrease)
            if abilityIncrease < 0:
                abilityIncrease = 0
                print "Let's keep it between 0 and 5, shall we?\nLower limit of 0 selected."
            elif abilityIncrease > 5:
                abilityIncrease = 5
                print "Let's keep it between 0 and 5, shall we?\nUpper limit of 5 selected."
            abilityScore = abilityScore + abilityIncrease
            character[ability] = abilityScore
            print '%s --> %d\n' % (ability, abilityScore)

generateAbilityScores()

print character.items()

# Adjust ability scores according to class and race.

# Assign equipment.

# Assign a feat.

# Create availableSkills list.
availableSkills = ['Alchemy', 'Animal empathy', 'Appraise', 'Balance', 'Bluff', 'Climb', 'Concentration', 'Craft', 'Decipher Script', 'Diplomacy', 'Disable Device', 'Disguise', 'Escape Artist', 'Forgery']

# Assign skillRanks.
skillRanks = 4

# classSkillCost = 

# nonClassSkillCost = 

# Assign skills.

# Create availableSpells list.
# availableSpells = []