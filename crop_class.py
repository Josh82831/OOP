import random

class Crop:
  """A generic food crop"""
  
  #constructor
  def __init__(self, growth_rate, light_need, water_need):
    #set the attributes with an initial Value
    self._growth = 0
    self._days_growing = 0 
    self._growth_rate = growth_rate
    self._light_need = light_need
    self._water_need = water_need
    self._status = "Seed"
    self._type = "Generic"

  def needs(self):
    return{"light need" : self._light_need, "water need" : self._light_need}
  
  def report(self):
    return{"type" : self._type, "status" : self._status, "growth" : self._growth, "days growing" : self._days_growing}

  def _update_status(self):
    if self._growth > 15:
      self._status = "Old"
    elif self._growth > 10:
      self._status = "Mature"
    elif self._growth > 5:
      self._status = "Young"
    elif self._growth > 0:
      self._status = "Seedling"
    else:
      self._status = "Food"

  def grow(self, light, water):
    if light >= self._light_need and water >= self._water_need:
      self._growth += self._growth_rate
    self._days_growing +=  1
    self._update_status()

def auto_grow(crop, days):
  for day in range(days):
    light = random.randint(1,10)
    water = random.randint(1,10)
    crop.grow(light, water)

def manual_grow(crop):
  valid = False
  while valid == False:
    try:
      light = int(input("Input light value (1 - 10)"))
      if 1 <= light <= 10:
        valid = True
      else: 
        print("Value entered invalid enter value between 1 and 10")
    except ValueError:
      print("Value entered invalid enter value between 1 and 10")
  valid = False
  while not valid:
    try:
      water = int(input("Input water value (1 - 10)"))
      if 1 <= water <= 10:
        valid = True
      else: 
        print("Value entered invalid enter value between 1 and 10")
    except ValueError:
      print("Value entered invalid enter value between 1 and 10")
  crop.grow(light, water)

def display_menu():
  print("1. Grow manually over 1 day")
  print("2. Grow automatically over 30 days")
  print("3. Report staus")
  print("0. Exit test program")
  print("")
  print("Please select an option from the above menu")

def get_menu_choice():
  valid = False
  while not valid:
    try:
      choice  = int(input("Option Selected: "))
      if 0 <= choice <= 3:
        valid = True
      else:
        print("Please enter a valid option")
    except ValueError:
      print("Please enter a valid option")
  return (choice)

def manage_crop(crop):
  print("This is the crop managment program")
  print("")
  exit = False
  while not exit:
    display_menu()
    option = get_menu_choice()
    print("")
    if option == 1:
      manual_grow(crop)
      print("")
    elif option == 2:
      auto_grow(crop,30)
      print("")
    elif option == 3:
      print(crop.report())
      print("")
    elif option == 0:
      exit = True
  print("Thank you for using this managment program")

def main():
  smm = Crop(1,1,1)
  manage_crop(smm)
