from enum import Enum
class Engine_emission_category(Enum):
    BS4=1
    BS6=2
    BS6_PHASE_2=3

class Car_type(Enum):
    SEDAN=1
    SUV=2
    OTHER=3
class Car:
    def __init__(self,m_reg_id:str,m_car_chassis_length:float,m_car_seat_count:float,m_car_engine_emission_caregory:Engine_emission_category,m_car_type:Car_type):
        self._reg_id=m_reg_id
        self._chassis_length=m_car_chassis_length
        self._seat_count=m_car_seat_count
        self._engine_emission_category=m_car_engine_emission_caregory
        self._car_type=m_car_type
    
    def __repr__(self):
        return f"{self.__dict__}"
    