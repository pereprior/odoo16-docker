import typesRol as type
from pokemon import Pokemon as Pkm
import pokemon as pkm

'''
Imprimir los datos con un pequeño intervalo de tiempo en cada letra
'''

if __name__ == "__main__":
    move1 = pkm.Move("Fire Blast",type.Fire(),pkm.MoveCategory.SPECIAL.value,110,85,5)
    move2 = pkm.Move("Mega Punch",type.Normal(),pkm.MoveCategory.PHYSICAL.value,80,95,15)
    move3 = pkm.Move("Hydro Pump",type.Water(),pkm.MoveCategory.SPECIAL.value,110,85,5)
    move4 = pkm.Move("Skull Bash",type.Normal(),pkm.MoveCategory.PHYSICAL.value,70,100,15)

    myPokemon = Pkm("Charizard",type.Fire(),[move1,move2],{"attack":84,"defense":78,"sattack":109,"sdefense":85,"speed":100,"hp":78},50)
    enemyPokemon = Pkm("Blastoise",type.Water(),[move3,move4],{"attack":83,"defense":100,"sattack":84,"sdefense":100,"speed":78,"hp":79},50)
    
    print(myPokemon)
    print(enemyPokemon)

    #myPokemon.turn(enemyPokemon)
    move1.typeRol(myPokemon,enemyPokemon)
    move2.typeRol(myPokemon,enemyPokemon)
    move3.typeRol(enemyPokemon,myPokemon)
    move3.typeRol(enemyPokemon,enemyPokemon)