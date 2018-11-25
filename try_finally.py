def func(a):
    tmp = 0
    try:
        return 2
        tmp = 10 / a
        print("after cal")
    except Exception as e:
        print("==>" + str(e) + "<===")
        return 1
    finally:
        print("always run?")
    return tmp


print(func(2))
print("")
print(func(0))
print("")
print(func(3))
