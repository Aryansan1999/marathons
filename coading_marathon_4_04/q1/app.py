from operations import convert_uppercase,convert_lowercase,remove_vowels,remove_special_characters,count_string_length
def main():
   
    n=int(input("Enter number of data "))
    data=[]
    for i in range(n):
        data.append(input())
    while True:
        print("Press 1 to convert to upper case")
        print("Press 2 to convert to lower case")
        print("Press 3 to remove vowels")
        print("Press 4 to remove special characters")
        print("Press 5 to count string length")
        print("Press 6 to quit")
        choice=int(input("Enter your choice: "))
        
        if choice==1:
            print(convert_uppercase(data))
            

        if choice==2:
            print(convert_lowercase(data))
        
        if choice==3:
            print(remove_vowels(data))

        if choice==4:
            print(remove_special_characters(data))

        if choice==5:
            print(count_string_length(data))

        if choice==6:
            break
if __name__=="__main__":
    main()