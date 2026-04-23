# main logic for battling
# pretty much just assumes that its a battle between 2 pokemons, 

class PokemonBattle:
    def __init__ (self, pokemon_a, pokemon_b):
        self.a = pokemon_a
        self.b = pokemon_b
        self.attackTurn = 0

    def turn(self):
        return self.attackTurn%2