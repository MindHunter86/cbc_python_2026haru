def input_scores(name):
    print(f'{name}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点？ >> '))
    database = int(input('データベースの得点？ >> '))
    security = int(input('セキュリティの得点？ >> '))
    scores = [ network, database, security ]
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    return avg

def output_result(name, avg):
    print(f'{name}sanno平均点は{avg}です。')

# 入力した得点をリストにして返す
asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')

# 得点リストをもとに平均点を計算
asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)

# 結果を出力
output_result('浅木',asagi_avg)
output_result('松田',matsuda_avg)