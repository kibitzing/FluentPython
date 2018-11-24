import abc,random

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(selfself, iterable):
        """iterable의 항목들을 추가한다."""

    @abc.abstractmethod
    def pick(self):
        """무작위로 항목을 하나 제거하고 반환한다.
        객체가 비어 있을 때 이 메서드를 실행하면 'LookupError'가 발생한다."""

    def loaded(self):
        """최소 한 개의 항목이 있으면 True를, 아니면 False를 반환한다."""
        return bool(self.inspect())

    def inspect(self):
        """현재 안에 있는 항목들로 구성된 정렬된 튜플을 반환한다."""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            self.load(items)
            return tuple(sorted(items))
### Yesterday's Code 

### Today's Code
class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()

class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))

@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

        load = list.extend

        def loaded(self):
            return bool(self)

        def inspect(self):
            return tuple(sorted(self))

# Tombola.register(TomboList)

print(issubclass(TomboList, Tombola))
t = TomboList(range(100))
print(isinstance(t, Tombola))
print(TomboList.__mro__)

