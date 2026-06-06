keyword = str(input("キーワードを入力 >> "))
letter = str(input("探す文字を入力 >> "))

count = 0
for i in keyword:
    if i == letter:
        count += 1

print(count)
