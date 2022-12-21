import items, enemies, actions, world
import sound

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEarth())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveMars())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveMercury())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveVenus())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewSolarSystem())

        return moves


class StartingRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You find yourself in a space with a flickering torch on the galaxy.
        You can make out four paths, each equally as mystery and foreboding.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
            if the_player.hp <=0:
                sound.Lose()

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Back(tile=self), actions.Shoot(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class MilkyWayGalaxy(MapTile):  # EmptyCavePath
    def intro_text(self):
        return """
        Another unremarkable part of the Milky-way Galaxy. You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class Aliens(EnemyRoom):  # GiantSpiderRoom
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Aliens())

    def intro_text(self):
        sound.AliensSound()
        if self.enemy.is_alive():
            return """
            A giant Aliens in front of you!
            """
        else:
            return """
            The corpse of a Aliens on the ground.
            """


class Ghost(EnemyRoom):  # WolfRoom
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ghost())

    def intro_text(self):
        sound.Ghost()
        if self.enemy.is_alive():
            return """
             A Ghost jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead Ghost is on the ground.
             """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        sound.Dagger()
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class LeaveMilkyWayGalaxy(MapTile):  # LeaveCaveRoom
    def intro_text(self):
        return """
        You see a Milky way in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours ohhh ohhhh!
        """

    def modify_player(self, player):
        player.victory = True