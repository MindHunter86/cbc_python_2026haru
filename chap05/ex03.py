def calc_shikaku(a, b):
    return a * b

def calc_sankaku(base, height):
    return 0.5 * base * height

def calc_maru(radius):
    return radius**2 * 3.14

figure = int(input('1: 四角形 ; 2: 三角形 ; 3: 円 >> '))

if figure == 1:
    height = int(input('縦の長さ >> '))
    weight = int(input('横の長さ >> '))
    print(f'面積は{calc_shikaku(height, weight)}です')
elif figure == 2:
    base = int(input('横の長さ >> '))
    height = int(input('縦の長さ >> '))
    print(f'面積は{calc_sankaku(base, height)}です')
elif figure == 3:
    radius = int(input('raduisの長さ >> '))
    print(f'面積は{calc_maru(radius)}です')
else:
    print('no such figure')