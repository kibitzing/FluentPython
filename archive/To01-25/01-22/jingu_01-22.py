# Created by Jingu Kang on 01-22
# reference: Fluent Python by Luciano Ramalho
# learned how @property works, and overriding classes and objects


# class LineItem:
#     def __init__(self, description, weight, price):
#         self.description = description
#         self.weight = weight
#         self.price = price
#
#     def subtotal(self):
#         return self.weight * self.price
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, value):
#         if value > 0:
#             self.__weight = value
#         else:
#             raise ValueError('value must be >0')
#

class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self.__weight

    def set_weight(self,value):
        if value > 0 :
            self.__weight = value
        else:
            raise ValueError('value must be >0')

    weight = property(get_weight, set_weight)


raisins = LineItem('Golden raisins', 10, 8)
print(raisins.subtotal())

# raisins = LineItem('Golden raisins', 0, 8)
# print(raisins.subtotal())

class Class:
    data = 'the class data attr'
    @property
    def prop(self):
        return 'the prop value'

obj = Class()
print(Class.data)
print(vars(obj))
print(obj.data)
obj.data = 'bar'
print(vars(obj))
print(obj.data)
print(Class.data)
