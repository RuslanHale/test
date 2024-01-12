class Place():
  def __init__(self, height, width):
    self.height = height
    self.width = width

    # Create place upon initialization
    self.matrix = [['_'] * self.width for i in range(self.height)]

  def show_place(self):
    for row in self.matrix:
      print(*row)

  def tank_position(self, tank):
    self.matrix[tank.y][tank.x] = tank.brand


class TanksDivision():
  def __init__(self, division):
    self.division = []


class Tank():
  all_tanks = []
  def __init__(self, place, brand, x, y):
    self.health = 100
    self.brand = brand
    self.x = x
    self.y = y
    Tank.all_tanks.append(self)
    place.tank_position(self)



# ----------------------------------------------------------------
# Для консольной версии:
  def shot(self, place, x, y):
    print(f'Стреляет {self.brand}')
    if place.matrix[y][x] == '_':
      print('Промах')
      place.matrix[y][x] = 'O'
    else:
      print('Попадание')
      place.matrix[y][x] = '*'
      for tank_prey in Tank.all_tanks:
        if tank_prey.x == x and tank_prey.y == y:
          tank_prey.health -= 100
          print(f'Убит {tank_prey.brand}')

def score():
  for i in range(len(Tank.all_tanks)):
    print(i + 1, Tank.all_tanks[i].brand, Tank.all_tanks[i].health)








