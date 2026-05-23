print("enter numbers for summarize")
num = 1
sum = 0
while num != 0:
    num = int(input("your number >>").strip() or 0)
    sum += num

print(f"sum of numbers {sum}")