from vehicle import Vehicle,VehicleType,PermitType,ChassisType,PrivateVehicle,ComercialVehicle

def create_objects(data):
    v1=Vehicle("e101",12000,PrivateVehicle(VehicleType.SEDAN),ComercialVehicle(ChassisType.LADDER_FRAME,PermitType.NATIONAL))
    v2=Vehicle("e102",32000,PrivateVehicle(VehicleType.SUV),ComercialVehicle(ChassisType.MONOCOQUE,PermitType.STATE))
    data.append(v1)
    data.append(v2)

def count_matching_vehicle(data,c_type):
    
    count=0     #counter variable for counting number of matching chassis type
    for value in data:
        if value._chassis_type==c_type:
            count+=1
    return count

def are_all_price_below_thresold(data,thresold):
    default_answer=True     #assuming all price is below thresold
    for value in data:
        if value._price>90000:  #if price above thresold
            default_answer=False    #storing false
    return default_answer

def return_total_insurance(data):
    sum=0
    for value in data:
        sum+=value.calculate_rto_charges()  #calculating sum for of RTO Charges
    return sum

def return_permit_cost_of_given_id(data,id):
    isFound=False
    for value in data:
        if id==value._reg_number:
            isFound=True
            value.calculate_permit_cost()
    if not isFound:
        raise ValueError("Entered registration number not found in database")  #if id is not found raising error
def display_data(data):
    for value in data:
        print(data)