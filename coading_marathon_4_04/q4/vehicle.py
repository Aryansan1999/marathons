from enum import Enum
class VehicleType(Enum):
    PRIVATE=1
    COMMERCIAL=2
    RENTAL=3

class ChassisType(Enum):
    MONICOQUE=0
    LADDER_FRAME=1
    OTHER=2

class Chassis():
    def __init__(self,length:float,width:int,type:ChassisType):
        self._length=length
        self._width=width
        self._type=type
        
    def __repr__(self):
        return f"{self.__dict__}"

class Vehicle:
    def __init__(self,reg_number:str,price:float,vehicle_type:VehicleType,chassis:Chassis):
        self._reg_number=reg_number
        self._price=price
        self._vehicle_type=vehicle_type
        self._chassis=chassis
        
    def __repr__(self):
        return f"{self.__dict__}"
