from operations import * #Importing operations pythone file


print("\n\t\t\t\t\t\t\t            Blue Technolgies")
print("\n\t\t\t\t\t\t\t           Jawalakhel,lalitpur")
print("\n")
print("------------------------------------------------------------------Welcome to the store------------------------------------------------------")
print("\n")
print("\n")
file = open("laptop.txt.txt","r")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
print("S.No","\t Name of the Laptop","\tlaptop Brand","\t\tPrice","\t\tQuantity","\tProcessor Details","\tGraphic Card")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
i=1
for line in file:
    laptop_details = line.strip().split(",")
    print("{:<10}{:<25}{:<21}{:<19}{:<14}{:<23}{:<15}".format(i, laptop_details[0], laptop_details[1], laptop_details[2], laptop_details[3], laptop_details[4], laptop_details[5]))
    i+=1

print("--------------------------------------------------------------------------------------------------------------------------------------------")
print("\n")




#function to buy laptop from the the company 
start = 0
def buy_laptop_from_the_shop():
    Customer_name = input("Please enter your name: ")
    print("")
    print("What would you like to do:")
    print("1.Buy laptop")
    print("2.Display available laptop")

    valid_option = False
    while valid_option ==False:
        try:
            option =int(input("\nPlease enter one from the two options:"))
            if option == 1 or option == 2:
                valid_option =True
            elif option < 1 or option > 2:
                print("The following option is not available, Please try again")
        except:
            print("Inavalid Input. Please choose from the given option.")
        #prints an error message when an invalid input is enteres
    if option == 1:
        buy(Customer_name)
    elif option == 2:
        laptop_file = file_data("laptop.txt.txt")
        data = data_list(laptop_file)
        display(data)
        return




#Function to sell laptop to the shop 
def sell_laptop_to_shop():
    Seller_name = input("Please enter your name or the company name: ")
    print("")
    print("What would you like to do:")
    print("1.sell laptop")
    print("2.Display laptops in the store")

    valid_option = False
    while valid_option ==False:
        try:
            option =int(input("\nPlease enter one from the two options:"))
            if option == 1 or option == 2:
                valid_option =True
            elif option < 1 or option > 2:
                print("The following option is not available, Please try again")
            #prints an error message when an invalid input is enteres
        except:
            print("Inavalid Input. Please choose from the given option.")
    if option == 1:
        sell(Seller_name)
    elif option == 2:
        laptop_file = file_data("laptop.txt.txt")
        data = data_list(laptop_file)
        display(data)
 




#Asks the user if they would like to buy sell or exit from the system
while start == 0:
    print("what would you like to do:")
    print("Press 1 to buy Laptop")
    print("Press 2 to sell laptop")
    print("Press 3 to exit from the system" )
    select = int(input("->"))
    if select==1:
        buy_laptop_from_the_shop()
    if select==2:
        sell_laptop_to_shop()
    if select==3:
        print("\nThank You please visit again",)
        start = 0
        break        

