# Магазин: разделяем обязанности
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=abs(round(price))
class ShoppingCart:
    def __init__(self):
        self.cart=[]
    def add_product(self,product, quantity=1):
        position={'product':product, 'qty':quantity }
        self.cart.append(position)
def print_receipt(number_cart):

    summa=0
    for i in number_cart.cart:
        summa+=(i['product'].price*i['qty'])
        print(f'{i['product'].name}:{i['product'].price}x{i['qty']}={(i['product'].price)*i['qty']}')
    return print(f'Итого: {summa}')
hleb=Product('Хлеб',50)
moloko=Product('Молоко',80)
cart1=ShoppingCart()
cart1.add_product(moloko,quantity=5)
cart1.add_product(hleb,quantity=10)
print_receipt(cart1)