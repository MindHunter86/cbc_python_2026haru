total = 0
counter = 0
while counter <= 100:
    total += counter
    if counter != 100:
        print(f"{counter} + ", end="")
    else:
        print(f"{counter}", end="")
    counter += 1

print("")
print(f"total is {total}")