class Item:
   def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

   def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other

   def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            return self.price - other

   def __mul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other, int):
            return self.price * other

   def __truediv__(self, other):
        if isinstance(other, Item):
            return self.price / other.price
        elif isinstance(other, int):
            return self.price / other


item_1 = Item('Видеокарта', 30000, 1)
item_2 = Item('Процессор', 20000, 0.3)
total_price_plus = item_1 + item_2
total_price_minus = item_1 - item_2
total_price_multiplied_by = item_1 * item_2
total_price_divided_by = item_1 / item_2
print(total_price_plus)
print(total_price_minus)
print(total_price_multiplied_by)
print(total_price_divided_by)
