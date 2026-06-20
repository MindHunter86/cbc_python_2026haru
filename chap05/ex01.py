def moji_print(moji, kaisu):
    print(f'{kaisu}回目:{moji}')

moji = str(input('表示する文字列を入力してください。>> '))
kaisu = int(input('繰り返す回数を入力してください。 >> '))

for i in range(1, kaisu + 1):
    moji_print(moji, i)