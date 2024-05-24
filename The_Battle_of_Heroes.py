# from abc import ABC, abstractmethod
import random


class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, character):
        self.attack_power += self.attack_power * random.randint(-10, 10)
        character.health -= self.attack_power
        print(f'{self.name} атаковал {character.name}, и нанёс {self.attack_power} очков урона.')
        print(f'У {character.name} осталось {character.health} очков здоровья.')

    def is_alive(self):
        return self.health > 0



