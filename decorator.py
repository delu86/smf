def before_after(f):
    def decorator():
        print('before')
        f()
        print('after')
    return decorator

@before_after
def hello_world():
    print('Hello world')

def logger(f):
    def decorator(x,y):
        print('Executing function '+f.__name__)
        f(x,y)
    return decorator
@logger
def add(x,y):
    print(x+y)

hello_world()
add(1,2)
    
