import player
from player import Player
 
class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
 
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class MoveMercury(Action):  #MoveNorth
    def __init__(self):
        super().__init__(method=Player.move_mercury, name='Jump to Mercury', hotkey='M') #n
 
 
class MoveVenus(Action): #MoveSouth
    def __init__(self):
        super().__init__(method=Player.move_venus, name='Jump to Venus', hotkey='V')  #s
 
 
class MoveEarth(Action): #MoveEast
    def __init__(self):
        super().__init__(method=Player.move_earth, name='Jump to Earth', hotkey='E') #e
 
 
class MoveMars(Action): #MoveWest
    def __init__(self):
        super().__init__(method=Player.move_mars, name='Jump to Mars', hotkey='W') #w
 
 
class ViewSolarSystem(Action): #ViewInventory
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=Player.viewSolarSystem, name='View Solor system', hotkey='V') #i

class Shoot(Action): #Attack
    def __init__(self, enemy):
        super().__init__(method=Player.shoot, name="Shoot", hotkey='SH', enemy=enemy) #a

class Back(Action): #Flee
    def __init__(self, tile):
        super().__init__(method=Player.back, name="Back", hotkey='B', tile=tile) #f


