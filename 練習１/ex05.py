height = float(input("身長(cm() >> "))
weight = float(input("体重(kg) >> "))

bmi = weight / ((height / 100) ** 2)
print(bmi)

if bmi < 18.5:
    print("低い")
elif bmi < 25:
    print("標準")
else:
    print("高い")