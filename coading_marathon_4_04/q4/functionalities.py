from vehicle import Vehicle,VehicleType,Chassis,ChassisType

def create_objects(data):
    id=input("Entyer id: ")
    price=int(input("Enter price: "))
    print("Press 1 for PRIVATE")
    print("Press 2 for COMMERCIAL")
    print("Press 3 for Rental")
    type=int(input("Enter type: "))
    length=float(input("Enter length of chassis: "))
    width=float(input("Enter width of chassis: "))
    print("Press 1 for MONICOQUE")
    print("Press 2 for LADDER_FRAME")
    print("Press 3 for OTHER")
    c_type=int(input("Enter type: "))
    data.append(Vehicle(id,price,type,Chassis(length,width,c_type)))

def count_matching_vehicle(data,type):
    count=0
    for value in data:
        if value._vehicle_type==type:
            count+=1

    return count   #no. of vehicles which has same type as input

def are_all_chassis_of_same_type(data,c_ctype):
    allSame=True
    for value in data:
        if value._chassis._type!=c_ctype:
            allSame=False
            break
    return allSame

def calculate_insurance_cost(data):
    insurance_cost=[]
    for value in data:
        if value._chassis._length<3:
            insurance_cost.append(4000)
        else:
            insurance_cost.append(8000)

    return insurance_cost   #insurance cost of each vehicle

def display_average_chassis_width(data):
    sum=0
    for value in data:
        sum+=value._chassis._width
    return sum/len(data) #average of width of all chassis

def display_data(data):
    for value in data:
        print(value)