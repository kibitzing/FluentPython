def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
        return cls.__name__.split('.')[-1]

def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))

class Overriding:

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set',self,instance,value)

class OverridingNoGet:
    """''__get__()''이 없는 오버라이딩 디스크립터"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class NonOverriding:
    """비데이터 디스크립터 혹은 가릴 수 있는 디스크립터라고도 한다."""

    def __get__(self, instance, owner):
        print_args('get',self,instance,owner)

class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))


obj = Managed()
print(obj.over)
print(Managed.over)
obj.over = 7
print(obj.over)
obj.__dict__['over'] = 8
vars(obj)
print(obj.over)

print(obj.over_no_get)
print(Managed.over_no_get)
obj.over_no_get = 7
print(obj.over_no_get)
obj.__dict__['over_no_get'] = 9
print(obj.over_no_get)
obj.over_no_get = 7
print(obj.over_no_get)

obj = Managed()
Managed.over = 1
Managed.over_no_get = 2
Managed.non_over = 3
print(obj.over, obj.over_no_get, obj.non_over)

obj = Managed()
print(obj.spam)
print(Managed.spam)
obj.spam = 7
print(obj.spam)
