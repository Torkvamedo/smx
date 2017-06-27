class Heroes():
    '''Class to create Heroes of our game'''
    def __init__(self, name, level, race):
        """initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """print all parameters of this hero"""
        discription = (self.name + 'level is   ' + str(self.level) + '  Race is '+ self.race + 'health  ' + str(self.health)).title()
        print(discription)

    def lvlup(self):
        """upgrade lvl of hero"""
        self.level += 1

    def move(self):
        """start moving """
        print("Hero " + self.name + "start moving")
# -------------------------------------------------------------------------------
class super_hero(Heroes):
    """Class to create Super Hero"""

    def __init__(self,name , level , race, magic_level):
        """initiate our super hero """
        super().__init__(name, level, race)   # инициализация класса Heroes и передача значений
        self.magic_level = magic_level
        self.magic = 100

    def make_magic(self):
        """use magic"""
        self.magic -= 10

    def show_hero(self):
        discription = (self.name + 'level is   ' + str(self.level) + '  Race is '+ self.race + 'health  ' + str(self.health
            + 'magic is: '+ self.magic)).title()
        print(discription)









# --------------MAIN-----------------------

my_hero1 = Heroes("Raynor ", 5 ," Elf ")
my_hero2 = Heroes("Jax ", 4, " Human ")
my_hero1.show_hero()
my_hero2.move()
my_hero1.lvlup()
my_hero1.show_hero()
my_hero = Heroes("Vurdalac  ", 10 , " undead ")
my_superher = super_hero (" Alios ", 90, " High Elf", 10 )
my_hero.lvlup()
my_hero.move()
my_hero.show_hero()
my_superher.magic
my_superher.lvlup()
my_superher.magic_level
my_superher.make_magic()
my_superher.race
my_superher.
