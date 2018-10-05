from animal_class import *

class Cow(animal):
    """A cow animal"""

    def __init__(self, name):
        super().__init__(2, 4, 2, name)
        self._type = "Cow"

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and food > self._food_need:
                self._weight += (self._growth_rate * 2)
            elif self._status == "Child" and water > self._food_need:
                self._weight += (self._growth_rate * 1.5)
            else: 
                self._weight += self._growth_rate
        self._days_growing += 1
        self.update_status()

