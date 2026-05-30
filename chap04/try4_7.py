data = [ 5, 8, 7, 2 ]

print()
print("jibunde tsukutta")
for i in data:
    if not isinstance(i, int):
        continue

    print(f'{i} | ', end='')

    for k in range(1, i+1):
        print('*', end='')

    print()

print()
print("second")
for i in data:
    print( str(i) + " | " + ("*" * i) )