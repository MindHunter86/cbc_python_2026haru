buf = ""
for i in range(1, 101):
    if i % 3 == 0:
        buf += "Fizz"
    if i % 5 == 0:
        buf += "Buzz"
    if len(buf) == 0:
        buf += str(i)
    
    print(buf)
    buf = ""