from q1 import unique_product,sold_product_id,product_sales_data,total_quantity,average_product_price,electronics_products_names,product_sales_generator,category_revenue
data_list=[]
from product import Products,Category
def main():
    flag=True
    p1=Products(1,"iPhone",999.99,2,Category.Electronics)
    p2=Products(2,"MacBook",1299.99,1,Category.Computers)
    p3=Products(1,"iPhone",999.99,3,Category.Electronics)
    p4=Products(3,"Samsumg TV",1499.99,1,Category.Electronics)
    p5=Products(2,"MacBook",1299.99,2,Category.Computers)
    data_list.append(p1)
    data_list.append(p2)
    data_list.append(p3)
    data_list.append(p4)
    data_list.append(p5)
    

    while flag:
        
        print("Press 1 for Unique Product category")
        print("Press 2 for sold product IDs")
        print("Press 3 for product sales data")
        print("Press 4 for total quantity sold")
        print("Press 5 for average product price")
        print("Press 6 for Electronics product names")
        print("Press 7 for product sales generator")
        print("Press 8 for category revenue")
        print("Press 9 to display all data")
        print("Press 10 to exit ")
        choice=int(input("Enter your choice: "))
        if choice>=1 and choice <=10:
            if choice==10:
                flag=False
                break
            if choice==1:
                unique_product(data_list)
            
            if choice==2:
                sold_product_id(data_list)

            if choice==3:
                product_sales_data(data_list)
            
            if choice==4:
                total_quantity(data_list)

            if choice ==5:
                average_product_price(data_list)

            if choice==6:
                electronics_products_names(data_list)

            if choice==7:
                product_sales_data(data_list)
            
            if choice==8:
                category_revenue(data_list)

            if choice==9:
                for i in data_list:
                    print(i)
        
            
        else:
            print("Please enter valid data")
if __name__=="__main__":
    main()