scores = [ 80, 20, 75, 60 ]
count = 0
while count < len(scores):
    if scores[count] >= 60:
        print("合格")
    else:
        print("不合格")
    count += 1

print(f"score sum {sum(scores)}")
print(f"average sum {sum(scores) / len(scores)}")