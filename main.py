from game_configuration import *
from back import score

if __name__ == "__main__":
    place_1.show_place()
    print()
    place_2.show_place()
    print()
    while True:
      for tank in red_team:
        coord_x, coord_y = int(input()), int(input())
        tank.shot(place_2, coord_x, coord_y)
        place_2.show_place()
        for i in blue_team:
          if i.x == coord_x and i.y == coord_y:
            blue_team.remove(i)
        score()
      for tank in blue_team:
        coord_x, coord_y = int(input()), int(input())
        tank.shot(place_1, coord_x, coord_y)
        place_1.show_place()
        for i in red_team:
          if i.x == coord_x and i.y == coord_y:
            red_team.remove(i)
        score()
