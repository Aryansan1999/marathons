from operation import search_car_by_id,find_n_lowest_priced_cars,add_new_entry,find_matching_varient_cars
from car import Car,Car_Varient
def main():
    flag=True
    while flag:
        print("Press 1 to saerch car by id")
        print("Press 2 to find n lowest car price")
        print("press 3 to add new car entry")
        print("Press 4 to find matching car varients")
        print("Press 5 to exit")
        choice=int(input("Enter your choice: "))
        if choice==5:
            break
        if choice==1:
            id=int(input("Enter car id: "))
            i=search_car_by_id(id)
            print(i)
        if choice ==2:
            lst=[]
            n=int(input("Enter value of n"))
            lst=find_n_lowest_priced_cars(n)
            print(lst)

        if choice==3:
            add_new_entry()
        if choice==4:
              print("press 1 for car varient BASE: ")
              print("press 2 for car varient ENHANCED: ")
              print("press 3 for car varient PRO: ")
              cat=int(input("Enter your choice"))
              con=Car_Varient(cat-1)
              find_matching_varient_cars(con)

        else:
            print("Invalid input")

if __name__=="__main__":
    main()