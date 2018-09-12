from collections import namedtuple
Food = namedtuple('Food', 'Menu price stock probability')
CheeseBurger = Food('Cheese Burger', 3200, 25, 0.78)
HamBurger = Food('Ham burger', 2500, 50, 0.99)
BeefBurger = Food('Beef burger', 4000, 20, 0.55)

#예상 판매량과 매출 계산
def calc_num_pre(Food):
    return Food.stock * Food.probability

def calc_sale_pre(Food):
    return Food.stock * Food.probability * Food.price


print("Cheese Burgers predicted : %d pieces , %d won" %(calc_num_pre(CheeseBurger),calc_sale_pre(CheeseBurger)))
print("Ham Burgers predicted : %d pieces , %d won" %(calc_num_pre(HamBurger),calc_sale_pre(HamBurger)))
print("Beef Burgers predicted : %d pieces , %d won" %(calc_num_pre(BeefBurger),calc_sale_pre(BeefBurger)))




