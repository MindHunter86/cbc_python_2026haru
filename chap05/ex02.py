def calc_menseki(a, b):
    return a * b

height = int(input('縦の長さ >> '))
weight = int(input('横の長さ >> '))

print(f'面積は{calc_menseki(height, weight)}です')