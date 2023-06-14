class User:

    def __init__(self, health, attack, damage):
        self.health = health
        self.attact = attack
        self.damage = damage


class Magic(User):
    pass


class Warrior(User):
    pass


class Archer(User):
    pass
