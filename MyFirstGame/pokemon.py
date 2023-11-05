from enum import Enum

class Pokemon:
    def __init__(self, name, types, moves, stats, level):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = stats['attack']
        self.defense = stats['defense']
        self.sattack = stats['sattack']
        self.sdefense = stats['sdefense']
        self.speed = stats['speed']
        self.hpBar = '===================='
        self.currentHp = stats['hp']
        self.level = level
    
    def __str__(self) -> str:
        return f"""
    {self.name}
    Types: {self.types}\n
    HP: {self.hpBar}
    Level_______________{self.level}
    Attack______________{self.attack}
    Defense_____________{self.defense}
    Special Attack______{self.sattack}
    Special Defense_____{self.sdefense}
    Speed_______________{self.speed}
    """

    def printMoves(self):
        for i, e in enumerate(self.moves, start=1):
            print(f"{i}.{e.name}", end="  ")
        print()

    def turn(self,enemy):
        self.printMoves()
        
        while True:
            user_input = input("Select one move: ")
            moves_number = len(self.moves)

            try:
                move_selected = int(user_input)
                if 1 <= move_selected <= moves_number:
                    move_selected -= 1
                    break
                else:
                    print(f"Please, select one move [1-{moves_number}]")
            except ValueError:
                print(f"Please, print the move number [1-{moves_number}].")
        
        print(self.moves[move_selected])

class Move:
    def __init__(self, name, type, category, power, accuracy, pp):
        self.name = name
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

    def typeRol(self,mine,enemy):
        if mine.types.name == self.type.name:
            self.power = self.power * 1.5
        
        for i,e in enumerate(self.type.OffWeak):
            if e == enemy.types.name:
                self.power *= 2
        
        for i,e in enumerate(self.type.OffResist):
            if e == enemy.types.name:
                self.power /= 2
        
        print(self.power)

    def __str__(self) -> str:
        return f"""
    {self.name}
    Type________{self.type}
    Category____{self.category}
    Power_______{self.power}
    Accuracy____{self.accuracy}
    PP__________{self.pp}
    """

class MoveCategory(Enum):
    PHYSICAL = "Physical"
    SPECIAL = "Special"
    STATUS = "Status"

    def __str__(self):
        return self.value
