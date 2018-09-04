def logit2(mess1,mess2):
    def logit(func): #无参装饰器放入并返回
        def new_func(*arg,**kwarg):
            print(mess1+" call %s" % func.__name__)
            func(*arg,**kwarg)
            print(mess2+" call %s" % func.__name__)
        return new_func
    return logit

@logit2("before fun", "after fun")
def hello(a):
    print("hello, world")
    if a>0: return 2


hello(3)