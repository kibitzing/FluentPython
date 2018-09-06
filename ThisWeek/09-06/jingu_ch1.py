import collections
from random import choice
from math import hypot

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._card)
    
    def __getitem__(self, position):
        return self._card[position]
"""    
beer_card  = Card('7', 'diamonds')
deck = FrenchDeck()
"""

# 정렬 법칙 알려주는 함수인듯 
def spades_high(card): 
    suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
    # .index -> 해당 값을 가진 인덱스를 반환해준다.
    rank_value = FrenchDeck.ranks.index(card.rank)
    # 4진수 처럼 만들어서 순서를 만들어 준다.
    return rank_value * len(suit_values) + suit_values[card.suit]

def spades_low(card): 
    suit_values2 = dict(spades = 0, hearts = 1, diamonds = 2, clubs = 3)
    # .index -> 해당 값을 가진 인덱스를 반환해준다.
    rank_value = FrenchDeck.ranks.index(card.rank)
    # 4진수 처럼 만들어서 순서를 만들어 준다.
    return rank_value * len(suit_values) + suit_values2[card.suit]

"""

for card in sorted(deck, key=spades_high):
    print(card)
    
print("spade low")
for card in sorted(deck, key=spades_low):
    print(card)    

"""
    
class Vector:
    def __init__(self, x = 0, y= 0):
        self.x = x 
        self.y = y
        
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
  
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
#    def __mul__(self, scalar):
 #       return Vector(self.x * scalar, self.y * scalar)
    #dot product only for vector(2,1) 약간 억지지만 ㅎㅎ
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


    