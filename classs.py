import random


class Tank:

    def __init__(self, model, health, min_damage, max_damage):
        self.model = model
        self.health = health
        self.damage = random.randint(min_damage, max_damage)

    def print_into(self):
        print(f'{self.model} имеет {self.health} очков здоровья и урон в {self.damage} единиц.')

    def health_down(self, enemy_damage):
        self.health -= enemy_damage
        print(f'Командир по нам попали. Осталось {self.health} здоровья')

    def shot(self, enemy):
        if enemy.health <= 0 or self.damage >= self.health:
            self.health = 0
            print(f'Экипаж погиб танка {enemy.model}.')
        else:
            enemy.health_down(enemy.damage)
            print(f'Есть пробитие. У противника осталось {enemy.health} единиц здоровья')


tank_1 = Tank('Т-34', 150, 90, 100)
tank_2 = Tank('Ягуар', 160, 80, 100)

tank_1.shot(tank_2)
tank_1.shot(tank_2)
tank_1.shot(tank_2)