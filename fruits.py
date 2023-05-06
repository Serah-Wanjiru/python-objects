class Fruit:
    quantity=0
    def __init__(self,name,quantity,price):
        self.fruit_name=name
        self.fruit_quantity=quantity
        self.fruit_price=price
    def add_fruits(self,quant):
        self.quantity+=quant
        return f"There are now {self.fruit_quantity} {self.fruit_name}"
    def remove_fruits(self,quant):
        self.quantity-=quant
        return f"There are now {self.quantity} {self.fruit_name}"
    def eat_fruits(self):
        return f"Here's a {self.fruit_name},enjoy!"
    fruit1=Fruit("Watermelon","banana","apples")
    fruit2=Fruit("Grapes","Passion","Dates")