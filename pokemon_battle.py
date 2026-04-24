# main logic for battling
# pretty much just assumes that its a battle between 2 pokemons, 

class PokemonBattle:
    def __init__ (self, pokemon_a, pokemon_b):
        self.a = pokemon_a
        self.b = pokemon_b
        self.__attackTurn = 0 # private, 

    def turn(self):
        return self.attackTurn%2
    
    def incturn(self):
        # increment turn 
        self.__attackTurn += 1
    
    # NUMBA PIEEEEEE