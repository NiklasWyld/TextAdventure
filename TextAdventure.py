from termcolor import colored
import random

# W = Weg (Nichts)
# G = Gegner
# E = Loot (Essen)
# L = Loot (Equipment)
# S = Spieler

# 7 x 7 (Spawn = 4, 4)

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

running = True
map = []
health = 15

x, y = 4, 4 # -1, -1

objects = ['W', 'G', 'E', 'L']
inventory = []

enemies = [Enemy('Glumando', 5, 0.5), Enemy('Pekanos', 2, 2), Enemy('Monisis', 8, 1)]

for i in range(7):
    object = random.choices(objects, weights=(60, 20, 10, 5), k=7)
    map.append(object)
    if i == 3:
        map[y-1][x-1] = 'S'

print(map)

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
    action = input('Wohin möchtest du gehen: ')
    action = action.lower().strip()

    if action == 'n':
        y -= 1
        m = map[y - 1][x - 1]

        if m == 'W':
            print('Du bist nach Norden gegangen.\nDu hast nichts interresantes entdeckt.')
        elif m == 'G':
            print('Du bist auf einen Gegner gestoßen!')
            b = input('Möchtest du kämpfen (K) oder möchtest du weitergehen (W)?')
            b = b.lower().strip()
            if b == 'k':
                pass
            elif b == 'w':
                print('Du gehst weiter...')
            else:
                print('Das kenne ich nicht.')
        elif m == 'E':
            pass
        elif m == 'L':
            pass
        else:
            print('Ein Fehler ist aufgetreten, bitte versuche das Spiel neuzustarten.')

        map[y-1][x-1] = 'S'
        map[y][x-1] = 'W'
    elif action == 'w':
        pass
    elif action == 'o':
        pass
    elif action == 's':
        pass
    elif action == 'stop':
        print('\nDanke fürs Spielen!\n')
        exit()
    else:
        print('Ich weiß nicht was du meinst.')

    print(map)