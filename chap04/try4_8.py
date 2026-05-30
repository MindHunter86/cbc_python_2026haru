a = [ 1, 2, 3 ]
b = [ 4, 5, 6 ]
c = [ a, b ]

for array in c:
    for elem in array:
        print(f' {elem}', end='')
    print()

print()
print("second")
for array in c:
    print(*array, sep=" ")