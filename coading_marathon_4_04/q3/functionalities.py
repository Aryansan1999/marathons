from car import Car,Car_type,Engine_emission_category

def create_objects(data):
    c1=Car("c01",12,4,Engine_emission_category.BS4,Car_type.SEDAN)
    c2=Car("c02",13,5,Engine_emission_category.BS6,Car_type.SUV)
    c3=Car("c03",15,2,Engine_emission_category.BS6_PHASE_2,Car_type.OTHER)
    c4=Car("c04",11,4,Engine_emission_category.BS4,Car_type.SEDAN)
    data.update({"c01":c1})
    data.update({"c02":c2})
    data.update({"c03":c3})
    data.update({"c04":c4})
    return data

def add_new_car_entry(data):
    reg_id=input("Enter unique id of car: ")
    chassis_length=float(input("Enter chassis length: "))
    seat_count=float(input("Enter seat number: "))
    print("Press 1 for BS4")
    print("Press 2 for BS6.")
    print("Press 3 for BS6_PHASE_2")
    emission=int(input("Enter your choice: "))
    print("Press 1 for SEDAN")
    print("Press 2 for SUV.")
    print("Press 3 for OTHER")
    type=int(input("Enter your choice: "))
    return data.update({reg_id:Car(reg_id,chassis_length,seat_count,emission,type)})

def count_given_type_cars(type,data):
    match=0
    for value in data.values():
        if value._car_type==type:
            count+=1
    return match #no of car types match


def return_car_type(reg_id,data):
    type_match=()
    isFound=False
    for value in data.values():
        if reg_id==value._reg_id:
            isFound=True
            type_match=(reg_id)+(value._car_type)
    if not isFound:
        raise ValueError("ID , not found in database")
    return type_match #tuple containing reg id and car type data

def Unique_Car_type(data):
    car_type_values=[]
    for value in data.values():
        car_type_values.append(value._car_type)
    return set(car_type_values) #set of unique car types avilable in data

def return_matching_instances(data):
    for value in data:
        conditon_match=list(filter(lambda x:x>10,value._chassis_length))
    return conditon_match #list satifying the predicate condition


def display_data(data):
    for value in data.values():
        print(value)
    return