# 6. Заказ и доставка 🚚🌶️
class Pickup:
    def calculate(self,delivery):
        return 0
class CourierDelivery:
    def calculate(self,subtotal):
        if subtotal<1000:
            return 0
        if subtotal>=1000:
            return 200
class Order:
    def __init__(self,delivery):
        self._subtotal=0
        self._total=0
        self._delivery=delivery
    def add_item(self,price):
        self._subtotal+=price
        return self._subtotal

    def subtotal(self):
        return str(self._subtotal)
    def total(self):
        self._total=self._subtotal+self._delivery.calculate(self._subtotal)
        return self._total
    def set_delivery(self,delivery):
        if isinstance(self._delivery, CourierDelivery) or isinstance(self._delivery, Pickup):
            self._delivery=delivery
        elif isinstance(self._delivery, Pickup) or isinstance(self._delivery, FixedDelivery):
            self._delivery=delivery
        elif isinstance(self._delivery, CourierDelivery) or isinstance(self._delivery, FixedDelivery):
            self._delivery=delivery
        return self._delivery
class FixedDelivery:
    def __init__(self,fee):
        self.fee=fee
    def calculate(self,subtotal):
        return self.fee
order=Order(Pickup())
order.add_item(200)
order.add_item(1000)
print(order.subtotal())
print(order.total())
order.set_delivery(FixedDelivery(1000))
print(order.total())