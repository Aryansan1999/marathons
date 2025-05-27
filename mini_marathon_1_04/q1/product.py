from enum import Enum
class Category(Enum):
    Electronics=0
    Computers=1

class Products():
    def __init__(self,product_id:int,product_name:str,price:int,quantity:int,category:Category):
        self._product_id=product_id
        self._product_name=product_name
        self._price=price
        self._quantity=quantity
        self._category=category

    def __repr__(self):
        return f"product detials-> product id:{self._product_id},product name: {self._product_name}, product price: {self._price},quantity: {self._quantity},category: {self._category}"
