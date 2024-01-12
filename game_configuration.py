from back import Place, Tank


place_1 = Place(4, 5)
place_2 = Place(4, 5)

tank_a = Tank(place_1, 'T1', x = 1, y = 2)
tank_b = Tank(place_1, 'T2', x = 2, y = 2)
tank_c = Tank(place_1,  'T3', x = 3, y = 3)

tank_1 = Tank(place_2, 'TA', x = 0, y = 1)
tank_2 = Tank(place_2, 'TB', x = 3, y = 1)
tank_3 = Tank(place_2,  'TC', x = 1, y = 2)


red_team = [tank_a, tank_b, tank_c]
blue_team = [tank_1, tank_2, tank_3]
