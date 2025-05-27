from functionalities import create_objects,add_new_car_entry,count_given_type_cars,return_car_type,Unique_Car_type,return_matching_instances,display_data



def main():
    data={}
    while True:

        print("Press 1 to create 4 objects")
        print("Press 2 to add new car entry")
        print("Press 3 to count given type")
        print("Press 4 to return car type")
        print("Press 5 for unique car type")
        print("Press 6 to return matching instances")
        print("Press 7 to display data")
        print("Press 8 to exit")

        choice=int(input("Enter your choice: "))
        if choice==1:
            create_objects(data)

        if choice==2:
            add_new_car_entry(data)

        if choice==3:
            print("Press 1 to SEDAN")
            print("Press 2 to SUV")
            print("Press 3 for OTHER")
            type=int(input("Enter your choice: "))
            match=count_given_type_cars(type,data)
            print(match)

        if choice==4:
            reg_id=input("Enter car unique id: ")
            print(return_car_type(reg_id,data))

        if choice==5:
            print(Unique_Car_type(data))

        if choice==6:
            print(return_matching_instances(data))

        if choice==7:
            display_data(data)

        if choice==8:
            break
if __name__=="__main__":
    main()