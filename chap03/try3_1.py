score = int(input("your score >>"))
if score < 0 or score > 100:
    print("invalid score")
elif score > 90:
    print("S")
elif score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")