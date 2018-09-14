import bisect


dinner = {'삼겹살':13000,'생등심':19000,'특수부위':23000,'육회':25000,'순대국밥':7000,'육회비빔밥':9000,'꽃등심':22000,'송어회':30000,'광어회':20000,'오리로스':49000,'오리훈제':49000}
new_menu = {'우삼겹':12000,'무한리필':17000,'물회':30000,'평양냉면':9000,'김튀순':8000,'허니콤보':19000}

print(dinner)

dinner_price = [v for _,v in dinner.items()]
new_dinner_price = [v for _,v in new_menu.items()]
dinner_price.sort()
new_dinner_price.sort()
print(dinner_price)
print(new_dinner_price)

for i in range(len(new_dinner_price)):
    bisect.insort(dinner_price,new_dinner_price[i])
    print(dinner_price)

dinner.update(new_menu)
todaymenu = [k for k,v in dinner.items() if v <= dinner_price[6]]
print(todaymenu)

# bisect.insort(dinner_price,new_dinner_price)
# dinner.sort()
# new_menu.sort()
# bisect.bisect(dinner,new_menu)