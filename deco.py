def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print(';^_^;')
    return wrapper

@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요, {name}님!')
    # print(';^_^;')

@emoji_decorator
def en_hello(name):
    print(f'Hello, {name}!')

def add_emoji(name, func):
    func(name)
    print(';^__^;')



en_hello('aiden')
