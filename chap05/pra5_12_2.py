def input_scores(name):
    print(f'{name}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点？ >> '))
    database = int(input('データベースの得点？ >> '))
    security = int(input('セキュリティの得点？ >> '))
    scores = [network,database,security]
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    return avg

def output_result(name,avg):
    print(f'{name}さんの平均点は{avg}です')

num = int(input('何人分の処理をしますか >> '))

for i in range(num):
    name = input(f'{i + 1}人目：名前を入力してください >> ')
    # 得点を入力
    scores = input_scores(name)
    
    # 平均点を計算
    avg = calc_average(scores)
    
    # 結果を出力
    output_result(name,avg)
