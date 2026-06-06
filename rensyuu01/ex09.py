money_type = {
    1: 8,
    5: 9,
    10: 3,
    50: 2,
    100: 8,
    500: 1,
}

sum = 0
for tp, cnt in money_type.items():
    sum += tp*cnt

print(f'合計金額: {sum}円')