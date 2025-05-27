from functionalities import create_objects,count_matching_vehicle,are_all_price_below_thresold,return_total_insurance,return_permit_cost_of_given_id,display_data


def main():
    data=[]
    while True:

        print("Press 1 to create objects")
        print("Press 2 to count matching vehicles")
        print("Press 3 to cheak all price is below thresold")
        print("Press 4 to return calculate insurance cost")
        print("Press 5 to return permit cost for given id")
        print("Press 6 to display data")
        print("Press 7 to exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            create_objects(data)

        if choice==2:
            print("Press 1 for MONICOQUE")
            print("Press 2 for LADDER_FRAME")
            print("Press 3 for OTHER")
            type=float(input("Enter type: "))
            c=count_matching_vehicle(data,type)
            print(f"no Matching vehicle type found: {c}")

        if choice==3:
            
            thresold=float(input("Enter thresold value: "))
            print(f"all price below thresold: {are_all_price_below_thresold(data,thresold)}")            

        if choice==4:
            print(f"total Insurance cost of vehicle: {return_total_insurance(data)}")
            thresold=float(input("Enter thresold value: "))
        if choice==5:
            id=float(input("Enter "))
            print(f"Permit cost for given id is :{return_permit_cost_of_given_id(data,id)}")
            

        if choice==6:

            display_data(data)

        if choice==7:
            break

if __name__=="__main__":
    main()