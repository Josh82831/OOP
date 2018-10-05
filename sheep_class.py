from animal_class import *

class Sheep(animal):
    """A sheep animal"""

    def __init__(self, name):
        super().__init__(1, 2, 5, name)
        self._type = "Sheep"

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need:
                self._weight += (self._growth_rate * 1.5)
            elif self._status == "Child" and water > self._water_need:
                self._weight += (self._growth_rate * 1.25)
            else: 
                self._weight += self._growth_rate
        self._days_growing += 1
        self.update_status()

