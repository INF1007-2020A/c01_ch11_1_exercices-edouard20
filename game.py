"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	def __init__(self, name, power, min_level):
		self.name = name
		self.power = power
		self.min_level = min_level
		
	UNARMED_POWER = 20
	@classmethod
	def make_unarmed(cls):
    	#return(cls.UNARMED_POWER, "unarmed")
		return cls("Unarmed", cls.UNARMED_POWER, 1)
class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name, max_hp, attack, defense, level, hp):
    	self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp
	
	def get_weapon(self):
    	return self.__weapon
	
	@setter
	def set_weapon(self, weapon: "Weapon"):
    	if weapon is None:
    		weapon = Weapon.make_unarmed()
		elif weapon.min_level > self.level:
    		raise ValueError("Weapon level too high for user")

	def get_hp(self):
    	return self.__hp
	
	def set_hp(self, hp):
    	#if hp < 0:
    	#	self.hp = 0
		#elif hp > 100:
    	#	self.hp = 100
		self.__hp = utils.clamp(hp,0,self.max_hp)

	def computedamage(attaquant,defenseur: Character):
		random = random.randrange(0.85,1)
		
		if random.randint(1,16) = 1:
    		crit = 2 
		else:
    		crit = 1
		
		modifier = crit * random

		return ((2* attaquant.level / 5 + 2) * attaquant.weapon.power * 	\
			(attaquant.attack / defenseur.defense) / 50 + 2) * modifier # ,crit

def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	print(f"{attacker.name} used {attacker.weapon.name}")

	damage = computedamage(attacker, defender)
	if attacker.crit = 2:
		print("  Critical hit!")
	defender.hp -= damage
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	turn_counter = 0
	c1 = attacker
	c2 = defender
	print(f"{attacker.name} starts a battle with {defender.name}!")
	
	while c1.hp > 0 and c2.hp > 0:
		# TODO: Appliquer l'attaque
		deal_damage(attacker,defender)
		# TODO: Si le défendeur est mort
		if defender.hp <= 0
			print(f"{defender.name } is sleeping with the fishes.")
			break
		turn_counter += 1
		# Échanger attaquant/défendeur
		if turn_counter % 2 == 1:
    			c1 = defender
				c2 = attacker
		else:
    			c1 = attacker
				c2 = defender
	# TODO: Retourner nombre de tours effectués
		
	return turn_counter
