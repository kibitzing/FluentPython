"""
created by Jingu Kang 
2018-10-12
coding: utf-8
"""

def hello(stringHi, *friends, **professor):
    str1 = stringHi
    
    if friends:
        for i in friends:
            a = ', '.join(i)
        return str1 + a
    
    if professor:
        for d, p in professor.items:
            pp = ', '.join(p + '교수님')
print(hello('안녕하세요', 'Daeha', '근회', 'Sanghong', '승현', '지윤','성빈',  prof='lee'))


import random 
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from Empty BingoCage')
        
    def __call__(self):
        return self.pick()
    
    
bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())

print('----')

def tag(name, *content, cls=None, **attrs):
    """ make more than one html tag"""
    if cls is not None:
        attrs['class'] = cls
        
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
        for attr, value in sorted(attrs.items()))
    else:
        attr_str =''
        
    if content:
        return '\n'.join('<%s%s>%s</%s>' % 
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s/>' %(name, attr_str)
    
print(tag('br'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name='img'))
my_tag = {'name':'img', 'title':'Sunset Boulevard', 
          'src': 'sunset.jpg', 'cls':'framed'}
print(tag(**my_tag))