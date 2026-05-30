for i1 in range(1, 10):
    for i2 in range(1, 10):
        mul = i1 * i2
        if mul < 10:
            print(" ", end="")
        print(mul, end="\t")
    print()


print()
print()
print()

for i1 in range(1, 10):
    for i2 in range(1, 10):
        print("{: >4}".format(i1*i2), end="")
    print()