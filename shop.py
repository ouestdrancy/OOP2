from item import Item
from phone import Phone

item1 = Item("MyItem", 750)
item1.name = "OtherItem"
item1.apply_increment(0.2)
print(item1.price)

'''
item1 = Item("Watch", 100, 5)
item2 = Item("Camera", 500, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
phone1 = Phone("iPhone17", 900, 5, 1) #inherited
print(phone1.calculate_total_price())
print(Item.all)
print(Phone.all)
phone2 = Phone("iPhone X", 500, 5, 1)

#for instance in Item.all:
#    print(instance.name)
#print(Item.__dict__) #All attributes for Class lvl
#print(item1.__dict__) #All attributes for Instance lvl
item1.apply_discount()
print(item1.price)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

print(Item.is_int(4.1))
'''