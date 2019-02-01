# p657~p661
# created by Jingu Kang on 02-01
# reference: Fluent Python by Luciano Ramalho

# quite standard, but boring class implementation
class Dog:
    def __init__(self, name, weight, owner):
        self.name = name
        self.weight = weight
        self.owner = owner

rex = Dog('Rex', 30, 'Bob')

# another way
def record_factory(cls_name, field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):  # <5>
        values = ', '.join('{}={!r}'.format(*i) for i
                           in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __iter__=__iter__,
                     __repr__=__repr__)

    # type here is used to make a class!
    return type(cls_name, (object,), cls_attrs)

Dog = record_factory('Dog', 'name weight owner')
rex = Dog('Rex', 30, 'Bob')
print(Dog)
print(rex)