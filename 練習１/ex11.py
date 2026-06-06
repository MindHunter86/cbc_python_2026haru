keyword = str(input('キーワードを入力 >> '))
letter = str(input('探す文字は? >> '))

cnt = 0
for char in keyword:
    cnt += 1
    if char == letter:
        print(cnt)
        break