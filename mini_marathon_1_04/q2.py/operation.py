from car import Car,Car_Varient
data_dic={
}
name=(x for x in range(1,1000000))
def create_objects():
    c1=Car(101,2021,Car_Varient.BASE,12000)
    c2=Car(102,2022,Car_Varient.ENHANCED,15000)
    c3=Car(103,2023,Car_Varient.PRO,18000)
    c4=Car(104,2020,Car_Varient.BASE,11000)
    data_dic.update({"car01":c1,"car02":c2,"car03":c3,"car04":c4})

def search_car_by_id(car_id:int):
    
    for i in data_dic.values():
        if i._id_car==car_id:
            return i
    raise ValueError

def find_n_lowest_priced_cars(N:int):
    lowest_price=[]
    if len(data_dic)<N:
        raise ValueError
    else:
        new_dic=sorted(data_dic,data_dic[0]._price)
        for i in new_dic.values():
            j=1
            if j<=N:
                lowest_price.append(i)
            else:
                break
            j+=1
        return lowest_price
            
    

def add_new_entry():
    carID=int(input("Enter car id: "))
    carManufacturingYear=int(input("Enter car manufacturing year: "))
    carPrice=int(input("Enter car Price: "))
    print("press 1 for car varient BASE: ")
    print("press 2 for car varient ENHANCED: ")
    print("press 3 for car varient PRO: ")
    cat=int(input("Enter your choice"))
    con=Car_Varient(cat-1)
    key_name="cat"+str(next(name))
    obj_name="c"+str(next(name))
    obj_name=Car(carID,carManufacturingYear,con,carPrice)
    data_dic.update({key_name:obj_name})
    print("Input successfull")

def find_matching_varient_cars(varient:Car_Varient):
    match_list=[]
    for i in data_dic.values():
        if i._car_varient==varient:
            match_list.append(i)
    
    for j in match_list:
        print(j)



    


    
