test = input('何を記録しますか？ >> ')
file = open('diary.txt', 'a')
file.write(test + '\n')
file.close()