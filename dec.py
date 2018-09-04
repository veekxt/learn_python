
def dec(func):
    def new_func(*arg,**kwarg):
        print("will call %s" % func.__name__)
        func(*arg,**kwarg)
        print("end call %s" % func.__name__)
    return new_func

def dec2(func):
    def new_func(*arg,**kwarg):
        print("2=>will call %s" % func.__name__)
        func(*arg,**kwarg)
        print("2=>end call %s" % func.__name__)
    return new_func

def dec3(a,b):
    def dec2(func):
        def new_func(*arg, **kwarg):
            print("2=>will call %s" % func.__name__)
            func(*arg, **kwarg)
            print("2=>end call %s" % func.__name__)

        return new_func
    return dec2

@dec
@dec2
def  hello():
    print("hello")

hello()
