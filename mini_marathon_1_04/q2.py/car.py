from enum import Enum
class Car_Varient(Enum):
    BASE=0
    ENHANCED=1
    PRO=2
class Car():
    def __init__(self,id_car:int,car_manufacturing_year:int,car_varient:Car_Varient,car_price:int):
        self._id_car=id_car
        if(car_manufacturing_year>=2000 and car_manufacturing_year <= 2025):
            self._car_manufacturing_year=car_manufacturing_year
        else:
            raise ValueError
        self._car_varient=car_varient
        self._car_price=car_price

    def __repr__(self):
        return f"car details id:{self._id_car},manufacturing year:{self._car_manufacturing_year},car varient:{self._car_varient},car price:{self._car_price}"

    def add(a,b):
        return a+b