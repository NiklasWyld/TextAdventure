from termcolor import colored
import random

# W = Weg (Nichts)
# G = Gegner
# E = Loot (Essen)
# L = Loot (Equipment)
# S = Spieler

# 7 x 7 (Spawn = 4, 4)

running = True
map = []

x, y = 4, 4 # -1, -1

o = ['W', 'G', 'E', 'L']

for i in range(7):
    p = random.choices(o, weights=(60, 20, 10, 5), k=7)
    map.append(p)
    if i == 3:
        map[y-1][x-1] = 'S'

print('Willkommen!\n')

print('Erklärung:\n'
      'Du kannst dich in alle vier Himmelsrichtungen bewegen mit N für Norden, S für Süden, W für Westen, O für Osten.\n'
      '  N  \n'
      'W   O\n'
      '  S  \n'
      'Du kannst jederzeit mit "STOP" das Spiel beenden.\n')

print('Du wachst in einer, mit hohem Gras bewachsenen, grünen Wiese auf. \n'
      'Du kannst dich an nichts mehr erinnern!\n'
      'Du siehst erstmal nichts.\n')

while running:
    a = input('Wohin möchtest du gehen: ')
    a = a.lower().strip()

    if a == 'n':
        y -= 1
        m = map[y - 1][x - 1]

        if m == 'W':
            print(colored('Du bist nach Norden gegangen.\nDu hast nichts interresantes entdeckt.', 'lightblue'))
        print(m)
    elif a == 'w':
        pass
    elif a == 'o':
        pass
    elif a == 's':
        pass
    else:
        print('Ich weiß nicht was du meinst.')

    print(map)