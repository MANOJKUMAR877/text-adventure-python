import random 
import items, world
import sound
class Player():
    def __init__(self):
        self.inventory = [items.Uranium(15), items.Knife(), items.Rock()] #Inventory on startup
        self.hp = 200 # Health Points
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up

    def back(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0   #Greater than zero value then you are still alive
 
    def viewSolarSystem(self):
        for item in self.inventory:
            print(item, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_mercury(self):
        self.move(dx=0, dy=-1)
 
    def move_venus(self):
        self.move(dx=0, dy=1)
 
    def move_earth(self):
        self.move(dx=1, dy=0)
 
    def move_mars(self):
        self.move(dx=-1, dy=0)

    def shoot(self, enemy):
        sound.ShootSound()
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
         if isinstance(i, items.Weapon):
            if i.damage > max_dmg:
                max_dmg = i.damage
                best_weapon = i
 
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            sound.Clap()
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
     action_method = getattr(self, action.method.__name__)
     if action_method:
                action_method(**kwargs)