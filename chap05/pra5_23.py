name = 'kazama'

def change_name():
    global name
    name = 'tsumura'
def hello():
    print(f'hello {name}')

change_name()
hello()