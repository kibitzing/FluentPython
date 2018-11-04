registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func
def delreg():
    registry = []
    print("레지스트리 비움")

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

@register
def f3():
    print('running f3()')

@register
def f4():
    print('running f4()')
    
def main():
    print('running main()')
    print('registry ->',registry)
    f1()
    f2()
    f3()
    f4()
    delreg()   
    
    #뭐야이거
if __name__ == '__main__':
    main()