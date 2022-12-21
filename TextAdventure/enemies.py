class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Aliens(Enemy):
    def __init__(self):
        super().__init__(name="Aliens", hp=50, damage=15)
 
class Flying_soccer(Enemy):
    def __init__(self):
        super().__init__(name="Flying_soccer", hp=30, damage=15)

class Meteorites(Enemy):
    def __init__(self):
        super().__init__(name="Meteorites", hp=20, damage=10)

class Ghost(Enemy):
    def __init__(self):
        super().__init__(name="Ghost", hp=25, damage=15)