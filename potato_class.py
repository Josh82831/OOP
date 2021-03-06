from crop_class import *

class Potato(Crop):
  """A potato crop"""

  #constructor
  def __init(self):
    #Call the parent class constructor with default values for potatoes
    super().__init__(1,3,6)
    self._type = "Potato"

  #override
  def grow(self, light, water):
    if light >= self._light_need and water >= self._water_need:
      if self._status == "Seedling" and water> self._water_need:
        self._growth += self._growth_rate * 1.5
      elif self._status == "Young" and water> self._water_need:
        self._growth += self._growth_rate * 1.25
      else:
        self._growth += self._growth_rate
    self._dats_growing += 1
    self._update_status()

def main():
  potato = Potato()
  print(potato.report())
  manual_grow(potato)
  print(potato.report())
