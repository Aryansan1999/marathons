from functionalities import create_objects,count_matching_vehicle,are_all_chassis_of_same_type,calculate_insurance_cost,display_average_chassis_width,display_data

def main():
    data=[]
    while True:

        print("Press 1 to create objects")
        print("Press 2 to count matching vehicles")
        print("Press 3 to cheak all chassis is same or not")
        print("Press 4 to return calculate insurance cost")
        print("Press 5 to display chassis width cost")
        print("Press 6 to display data")
        print("Press 7 to exit")

        choice=int(input("Enter your choice: "))
        if choice==1:
            create_objects(data)

        if choice==2:
            print("Press 1 for PRIVATE")
            print("Press 2 for COMMERCIAL")
            print("Press 3 for Rental")
            type=int(input("Enter type: "))
            c=count_matching_vehicle(data,type)
            print(f"no Matching vehicle type found: {c}")

        if choice==3:
            print("Press 1 for MONICOQUE")
            print("Press 2 for LADDER_FRAME")
            print("Press 3 for OTHER")
            c_type=int(input("Enter type: "))
            print(f"all chassis is same: {are_all_chassis_of_same_type(data,c_type)}")            

        if choice==4:
            print(f"Insurance cost of vehicle: {calculate_insurance_cost(data)}")

        if choice==5:
            print(f"Average chassis width is :{display_average_chassis_width(data)}")
            

        if choice==6:
            display_data(data)

        if choice==7:
            break

if __name__=="__main__":
    main()