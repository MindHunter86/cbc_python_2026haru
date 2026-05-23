sum = 0
for i in range(0, 100):
    if i % 10 != 0:
        sum += i
print(sum)

sum = 0
for i in range(0, 101, 1):
    if i % 10 != 0:
        sum += i
print(sum)