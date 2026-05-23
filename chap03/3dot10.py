print("全て質問にyまたはnで答えてください")
okane_akura = input("お金に余裕はありますか >>")
if okane_akura == "y":
    okane_suiteruka = input("お腹がすごく空いてますか>>")
    nomitai_kibunka = input("ビールを飲みたいですか >>")
    if okane_suiteruka == "y" and nomitai_kibunka == "y":
        print("焼き肉はいかがですか")
    elif okane_suiteruka == "y":
        print("カレーはいかがですか")
    elif nomitai_kibunka == "y":
        print("焼き鳥はいかがですか")
    else:
        print("パスタはいかがですか")
    yashoku_iruka = input("夜食は必要ですか >>")
    if yashoku_iruka == "y":
        print("コンビニのチキンはいかがですか")
else:
    print("お宅で食べましょう")
        