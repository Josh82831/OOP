from potato_class import *
from wheat_class import *
from sheep_class import *
from cow_class import *

class Field ():
    """Simulata a field tha can hold animals and crops"""
    def __init__(self, max_animals, max_crops):
        self._animals = []
        self._crops = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self, crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self, animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest_crop (self,position):
        return self._crops.pop(position)

    def remove_animal (self,position):
        return self._animals.pop(position)

def display_crops(crop_list):
    print()
    print("These crops are in this field")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos,crop.report()))
        pos += 1

def display_animals(animal_list):
    print()
    print("These animals are in this field")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos,animal.report()))
        pos += 1

def select_crop(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop: "))
        if selected in range(1, length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected - 1

def select_animal(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a animal: "))
        if selected in range(1, length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected - 1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)

def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    return field.remove_animal(selected_animal)





def main():
    newy = Field(5,2)
    newy.plant_crop(Wheat())
    newy.plant_crop(Potato())
    newy.add_animal(Sheep("Shaun"))
    newy.add_animal(Cow("Jim"))
    harvest_crop_from_field(newy)
    print(newy._crops)
    remove_animal_from_field(newy)
    print(newy._animals)

main()



