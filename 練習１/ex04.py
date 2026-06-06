members = [ 'tsumura', 'hashimoto' ]
print(members)

members.append('kazama')

todelete = str(input("誰を消除しまうか？ >> "))
members.remove(todelete)
print(members)