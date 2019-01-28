class LineItem1:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
    
# >>> raisins = LineItem('Golden raisins', 10, 6.95)
# >>> raisins.subtotal()
# 69.5
# >>> raisins.weight = -12
# >>> raisins.subtotal()
# -83.4


class LineItem2:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight # 비공개 속성인 __weight에 저장

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('음수는 안돼요') # 보호 장치


# >>> raisins.weight = -20
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 20, in weight
# ValueError: 음수는 안돼요


class LineItem3:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
        
    def subtotal(self):
        return self.weight * self.price
    
    def get_weight(self):  # 게터
        return self.__weight
    
    def set_weight(self, value):  # 세터
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('음수는 안돼요')
    
    weight = property(get_weight, set_weight)
    # property 객체 생성 후 클래스의 공개 속성에 할당


class Class:
    data = 'the class data attr'
    @property
    def prop(self):
        return 'the prop value'

# >>> obj = Class()
# >>> vars(obj)
# {}
# >>> obj.data
# 'the class data attr'
# >>> obj.data = 'bar'                      # 객체 속성 생성됨
# >>> vars(obj)                             # 객체 속성 생성 확인
# {'data': 'bar'}
# >>> obj.data
# 'bar'                                     # 객체 속성의 값을 가져옴
# >>> Class.data
# 'the class data attr'                     # Class.data 속성은 그대로
# >>> Class.prop
# <property object at 0x000001F49540CD18>   # 프로퍼티 객체 자체를 가져옴
# >>> obj.prop
# 'the prop value'
# >>> obj.prop = 'foo'
# Traceback (most recent call last):        # 객체의 prop 속성에 값 할당할 수 없음
#   File "<input>", line 1, in <module>
# AttributeError: can't set attribute
# >>> obj.__dict__['prop'] = 'foo'          # __dict__에 직접 할당은 가능
# >>> vars(obj)
# {'prop': 'foo', 'data': 'bar'}
# >>> obj.prop
# 'the prop value'
# >>> Class.prop = 'baz'                    # 덮어쓰면 프로퍼티 객체 사라짐
# >>> obj.prop
# 'foo'
