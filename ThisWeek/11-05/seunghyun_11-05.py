from array import array
import math
from datetime import datetime

class Vector2d:
    typecode = 'd'
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __iter__(self):
        return (i for i in (self.x, self.y))
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    def __str__(self):
        return str(tuple(self))
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    def angle(self):
        return math.atan2(self.y, self.x)


now = datetime.now()
print (format(now, '%H:%M:%S'))
print ("It's now {:%I:%M %p}".format(now))
print (format(now, "It's now %H:%M:%S"))
v1 = Vector2d(3, 4)
print (format(v1))

print (format(Vector2d(1, 1), 'p'))
print (format(Vector2d(1, 1), '.3ep'))
print (format(Vector2d(1, 1), '0.5fp'))
