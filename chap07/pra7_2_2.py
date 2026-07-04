srcfile = open('diary.txt', 'r')
dstfile = open('diary2.txt', 'a')

for line in srcfile:
    dstfile.write(line)

srcfile.close()
dstfile.close()