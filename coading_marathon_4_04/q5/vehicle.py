from enum import Enum
from abc import abstractmethod
class VehicleType(Enum):
    SEDAN=1
    SUV=2
    OTHER=3

class ChassisType(Enum):
    MONOCOQUE=0
    LADDER_FRAME=1
    OTHER=2

class PermitType(Enum):
    STATE=1
    NATIONAL=2

class Vehicle():
    def __init__(self,reg_number:str,price:float):
        self._reg_number=reg_number
        self._price=price

    def __repr__(self):
        return f"{self.__dict__}"
    
    @abstractmethod
    def calculate_rto_charges(self):
        pass


class PrivateVehicle(Vehicle):
    def __init__(self, reg_number:str, price:float,vehicle_type:VehicleType):
        super().__init__(reg_number, price)
        self._vehicle_type=vehicle_type

    def __repr__(self):
        return f"{self.__dict__}"
    
    def calculate_rto_charges(self):
        if self._vehicle_type==1:
            return 0.1*self._price
        else:
            return 0.2*self._price
        
    
class ComercialVehicle(Vehicle):
    def  __init__(self, reg_number:str, price:float,chassis_type:ChassisType,permitType:PermitType):
        super().__init__(reg_number, price)
        self._chassis_type=chassis_type
        self._permit_type=permitType

    def calculate_rto_charges(self):
        return 0.2*self._price

    def calculate_permit_cost(self):
        if self._permit_type==1:
            return 2000
        else:
            return 5000

