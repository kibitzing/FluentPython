from collections import abc
import re,reprlib


RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


class Foo:
    def __iter__(self):
        pass


s = Sentence('"The time has come," the Walrus said,')
print(s)

for word in s:
    print(word)

print(list(s))

print(s[0])
print(s[5])
print(s[-1])

print(issubclass(Foo, abc.Iterable))
f = Foo()
print(isinstance(f, abc.Iterable))



