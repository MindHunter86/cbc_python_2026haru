ages = [28, 50, "hitotsu", 20, 78, 25, 22, 10, "mumshimushi", 33]
samples = list()

for age in ages:
    if not isinstance(age, int):
        continue
    if age < 20 or age >= 30:
        continue
    samples.append(age)

print(samples)