types_chart = {"fire":
               {2: ["grass", "ice", "bug", "steel"], 0.5: [
                   "fire", "water", "rock", "dragon"]},
               "water":
               {2: ["fire", "ground", "rock"], 0.5: [
                   "water", "grass", "dragon"]},
               "grass":
               {2: ["water", "ground", "rock"], 0.5: [
                   "fire", "grass", "poison", "fly", "bug", "dragon", "steel"]}
               }


class Pokemon():

    def __init__(self, name, level, type, health, ko = False):
        self.name = name
        self.level = level
        self.type = type
        self.maximum_health = int(health * (1 + level/50))
        self.health = int(health * (1 + level/50))
        self.ko = ko

    def __repr__(self):
        return f"{self.name.capitalize()}: {self.health}/{self.maximum_health} | Level: {self.level}"

    def lose_health(self, damage):
        self.health -= damage
        if damage == 0:
            pass
        elif self.health > 0:
            print(f"{self.name} receives {damage} points of damage. {self.name} has {self.health}/{self.maximum_health} remaining health points.")
        else:
            self.health = 0
            self.ko = True
            print(
                f"{self.name} receives {damage} points of damage. {self.name} has been knocked out.")
            

    def regain_health(self):
        heal = self.maximum_health // 5
        self.health += heal
        if self.health > self.maximum_health:
            print(f"{self.name} recovers {heal - (self.maximum_health - self.health)} health points. {self.name} has {self.maximum_health}/{self.maximum_health} health points.")
            self.health = self.maximum_health
        else:
            print(
                f"{self.name} recovers {heal} health points. {self.name} has {self.health}/{self.maximum_health} health points.")

    def revive(self):
        self.ko = False
        self.health_points = self.maximum_health // 10
        print(f"{self.name} has been revived, recovering 10% of its maximum health points. {self.name} has {self.health}/{self.maximum_health} health points.")

    def attack_pokemon(self, target):
        damage = self.level * 10
        print(f"{self.name} attacks {target.name}.")
        if target.type in types_chart[self.type][2]:
            damage *= 2
            print("It is super effective!")
        elif target.type in types_chart[self.type][0.5]:
            damage //= 2
            print("It is not very effective...")
        elif target.type in types_chart[self.type][0]:
            damage = 0
            print("It has no effect...")
        target.lose_health(int(damage))


    def __add__(self, other):
        if type(other) == "int":
            return Pokemon(self.name, self.level + other, self.type, self.health)

    def __iadd__(self, other):
        if type(other) == "int":
            return Pokemon(self.name, self.level + other, self.type, self.health)
        


class Trainer():
    def __init__(self, name, pokemons, potions, active_pokemon, not_playable = "False"):
        self.name = name
        self.pokemons = pokemons
        self.potions = potions
        self.active_pokemon = pokemons[active_pokemon]
        self.not_playable = not_playable

    def __repr__(self):
        return self.name.capitalize()

    def heal_pokemon(self):
        if self.potions > 0:
            self.potions -= 1
            print(f"{self.name} uses a potion on {self.active_pokemon.name}.")
            self.active_pokemon.regain_health()

    def attack_trainer(self, target):
        print(f"{self.name} asks {self.active_pokemon.name} to attack {target.name}'s pokemon: {target.active_pokemon.name}.")
        self.active_pokemon.attack_pokemon(target.active_pokemon)
        if target.active_pokemon.ko:
            target.switch_pokemon()
        
    def switch_pokemon(self):
        available_pokemons = [pokemon for pokemon in self.pokemons if not pokemon.ko]
        if not available_pokemons:
            print("{self.name} loses the fight.")
            exit()
        if self.active_pokemon in available_pokemons:
            available_pokemons.remove(self.active_pokemon)
        if self.not_playable:
            self.active_pokemon = available_pokemons[0]
        else:
            [print(f"{index + 1}: {pokemon.name}") for index, pokemon in enumerate(available_pokemons)]
            pokemon_choice = None
            while pokemon_choice == None:
                try:
                    pokemon_choice = int(input("Select the pokemon you want to switch to: "))
                    if pokemon_choice > len(available_pokemons) or pokemon_choice < 1:
                        print("You didn't enter a valid option.")    
                        pokemon_choice = None
                except:
                    print("You didn't enter a valid option.")
                    pokemon_choice = None
            self.active_pokemon = available_pokemons[pokemon_choice - 1]
        print(f"{self.name} swicth to another pokemon. {self.active_pokemon.name} is ready to fight.")
  
        
bulbasaur = Pokemon("Bulbasaur", 1, "grass", 300)
charmeleon = Pokemon("Charmeleon", 20, "fire", 250)
squirtle = Pokemon("Squirtle", 10, "water", 250)
charizard = Pokemon("Charizard", 35, "fire", 250)
ivysaur = Pokemon("Ivysaur", 35, "grass", 400)
wartortle = Pokemon("Wartortle", 25, "water", 250)

red = Trainer("Red", [bulbasaur, squirtle, charizard], 7, 0)
blue = Trainer("Red", [ivysaur, wartortle, charmeleon], 3, 0, True)