from enum import Enum
from abc import abstractmethod

class Car():
    def __init__(self,m_id:str,m_price:float):
        self._m_id=m_id
        self._m_price=m_price
    
    @abstractmethod
    def calculate_insurance_cost():
        pass

class m_battery_type(Enum):
    LI_ION=0
    NI_CAD=1
    OTHER=2

class m_hybrid_setup_type(Enum):
    ELECTRIC_HYBRID=0
    HYDROGEN_HYBRID=1

class HybridCar(Car):
    def __init__(self, m_id:str, m_price:float,setup_type:m_hybrid_setup_type,m_fuel_capacity:int,m_hybrid_car_engine_cc:int):
        super().__init__(m_id, m_price)
        self._setup_type=setup_type
        self._m_fuel_capacity=m_fuel_capacity
        self._m_hybrid_car_engine_cc=m_hybrid_car_engine_cc

    def calculate_insurance_cost(self):
        if self._setup_type==m_hybrid_setup_type.ELECTRIC_HYBRID:
            return .1*self._m_price
        if self._setup_type==m_hybrid_setup_type.HYDROGEN_HYBRID:
            return 1*self._m_price

class EVCar(Car):
    def __init__(self, m_id, m_price,battery_type:m_battery_type,m_battrey_capacity:float):
        super().__init__(m_id, m_price)
        self._battery_type=battery_type
        self._battery_capacity=m_battrey_capacity

    def calculate_insurance_cost(self):
        return self._m_price*self._battery_capacity
    
### print.get(input(),"data not found,default msg")