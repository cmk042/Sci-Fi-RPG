"""
Module Name: characters.py

Description:
This module defines the Character and Race classes. It includes logic for
initializing character attributes, calculating stats, and handling race-specific details.

Author: Casey King
Date: 12/31/2024
"""
import csv, math

race_stats = {}
file_path = "race_stats.csv"
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        race_name = row.pop('Race')
        race_stats[race_name] = {key: int(value) for key, value in row.items()}



class Character:
    """
    Character Representation in the game.

    Attributes:
        name (str): The name of the character.
        race (Race): The race object representing the character's species.
        level (int): The level of the character.
        health (int): The health stat of the character, derived from race and level.
        strength (int): The strength stat of the character, derived from race and level.
        skills (dict): A dictionary of skills the character possesses.
        equipment (dict): A dictionary of equipped items (e.g., weapon, armor).
    
    Methods:
        calculate_stat(stat_name): Calculates the stat value based on race and level.
    """
    def __init__(self, name, race, level, genetics):
        self.name = name
        self.race = race
        self.base_stats = race_stats[race]
        self.level = level
        self.genetics = genetics
        self.rem_hp = 150
        self.rem_cp = 225
        self.rem_sp = 225

        self.health_points = {'Health': 0, 'Strength': 0, 'Agility': 0, 'Stamina': 0}

        self.combat_points = {'Swordsmanship': 0, 'Marksmanship': 0, 'Detonations': 0,
                         'Sorcery': 0, 'Plasmancy': 0, 'Striking': 0,'Wrestling': 0}
        
        self.skill_points = { 'Engineering': 0, 'Hacking': 0, 'Stealth': 0, 'Charisma': 0,
                           'Healing': 0 }
        
        self.stats = {'Health': 0, 'Strength': 0, 'Agility': 0, 'Stamina': 0, 'Attack': 50,
                       'Defense': 50, 'Swordsmanship': 0, 'Marksmanship': 0, 'Detonations': 0,
                         'Sorcery': 0, 'Plasmancy': 0, 'Striking': 0,'Wrestling': 0,
                         'Engineering': 0, 'Hacking': 0, 'Stealth': 0, 'Charisma': 0,
                           'Healing': 0}
        
        for stat in self.stats:
            self.calculate_stat(stat)
        
        self.equipment = {"Weapon1": None, "Weapon2": None, "Weapon 3": None, "Helmet": None, "Body Armor": None }



    def calculate_stat(self, stat_name):
        if stat_name in self.health_points:
            self.stats[stat_name] = math.floor( (self.base_stats[stat_name]
                                                  * 1.1 + self.genetics[stat_name]) 
                                                  * 2 * self.level / 90)
        elif stat_name in ["Marksmanship", "Swordsmanship"]:
            self.stats[stat_name] = math.floor((self.base_stats["Dexterity"]
                                                 * 0.9 + 1.1 * self.genetics["dexterity"])
                                                   * 2 * (math.sqrt(self.level)
                                                           + self.skill_points[stat_name]) / 100)
        elif stat_name in ["Engineering", "Hacking", "Healing"]:
            self.stats[stat_name] = math.floor((self.base_stats["Intelligence"]
                                                 + self.genetics["Intelligence"]) * 2 * 
                                                 (math.sqrt(self.level) + 
                                                  self.skill_points[stat_name]) / 100)
        elif stat_name == "Detonations":
            self.stats[stat_name] = math.floor((self.base_stats["Dexterity"]+self.genetics["Dexterity"]+self.base_stats["Intelligence"]
                                                 + self.genetics["Intelligence"]) * (math.sqrt(self.level) + 
                                                  self.skill_points[stat_name])/ 100)
        elif stat_name == "Sorcery":
            self.stats[stat_name] = math.floor((self.base_stats["Magic"] * 1.1
                                                 + .9 * self.genetics["Magic"]) * 2 * 
                                                 (math.sqrt(self.level) + 
                                                  self.skill_points[stat_name]) / 100)
        elif stat_name == "Plasmancy":
            self.stats[stat_name] = math.floor((self.base_stats["Stamina"] * .5
                                                 + 2* self.genetics["Plasmancy"]) * 
                                                 (math.sqrt(self.level) + 
                                                  3* self.skill_points[stat_name]) / 100)
        elif stat_name == "Wrestling":
            self.stats[stat_name] = math.floor((self.base_stats["Itelligence"] + self.genetics["Intelligence"]
                                                + self.base_stats["Agility"] + self.genetics["Agility"]
                                                + self.base_stats["Dexterity"] + self.genetics["Dexterity"]
                                                + self.base_stats["Stamina"] + self.genetics["Stamina"]
                                                + self.base_stats["Strength"] + self.genetics["Strength"]) * .6 *
                                                 (math.sqrt(self.level) + 
                                                  3* self.skill_points[stat_name]) / 100)
        elif stat_name == "Striking":
            self.stats[stat_name] = math.floor((self.base_stats["Itelligence"] + self.genetics["Intelligence"]
                                                + self.base_stats["Agility"] + self.genetics["Agility"]
                                                + self.base_stats["Dexterity"] + self.genetics["Dexterity"]
                                                + self.base_stats["Stamina"] + self.genetics["Stamina"]) * .8 *
                                                 (math.sqrt(self.level) + 
                                                  3* self.skill_points[stat_name]) / 100)
        elif stat_name == "Stealth":
            self.stats[stat_name] = math.floor((3*(self.base_stats["Agility"]+self.genetics["Agility"])+self.base_stats["Intelligence"]
                                    + self.genetics["Intelligence"]) * (math.sqrt(self.level) + 
                                    self.skill_points[stat_name])/ 200)
        elif stat_name == "Charisma":
            self.stats[stat_name] = math.floor((self.genetics["Sociability"]+math.sqrt(self.level))*self.skill_points[stat_name]/100)
        else:
            print("INVALID STAT")

