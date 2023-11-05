'''
class TypeSheet(Enum):
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    GRASS = "Grass"
    ELECT = "Electric"
    FIGHT = "Fighting"
    FLY = "Flying"
    ROCK = "Rock"
    GROUND = "Ground"
    STEEL = "Steel"
    POISON = "Poison"
    BUG = "Bug"
    GHOST = "Ghost"
    DARK = "Dark"
    PSY = "Psyquic"
    FAIRY = "Fairy"
    DRAGON = "Dragon"
    ICE = "Ice"
'''


class Type:
    def __init__(self):
        self.name = self.__class__.__name__
        self.OffWeak = []
        self.DefWeak = []
        self.OffResist = []
        self.DefResist = []
        self.OffInmune = []
        self.DefInmune = []

    def OffensiveRol(self):
        pass

    def DefensiveRol(self):
        pass

    def __str__(self) -> str:
        return self.name


class Normal(Type):
    def __init__(self):
        super().__init__()
        self.OffResist = ["Rock","Steel"]
        self.OffInmune = "Ghost"
        self.DefWeak = "Fighting"
        self.DefInmune = "Ghost"


class Fire(Type):
    def __init__(self):
        super().__init__()
        self.OffWeak = ["Bug","Steel","Grass","Ice"]
        self.OffResist = ["Rock","Fire","Water","Dragon"]
        self.DefWeak = ["Ground","Rock","Water"]
        self.DefResist = ["Bug","Steel","Fire","Grass","Ice","Fairy"]
        


class Water(Type):
    def __init__(self):
        super().__init__()
        self.OffWeak = ["Ground","Rock","Fire"]
        self.OffResist = ["Water","Grass","Dragon"]
        self.DefWeak = ["Grass","Electric"]
        self.DefResist = ["Steel","Fire","Water","Ice"]
        


class Grass(Type):
    def __init__(self):
        super().__init__()
        self.OffWeak = ["Ground","Rock","Water"]
        self.OffResist = ["Flying","Poison","Bug","Steel","Fire","Grass","Dragon"]
        self.DefWeak = ["Flying","Poison","Bug","Fire","Ice"]
        self.DefResist = ["Ground","Water","Grass","Electric"]