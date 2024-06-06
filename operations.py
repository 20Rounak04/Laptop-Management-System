from read import * #importing read python file
from write import * #importing write python file


# function created to display names of the laptop from the data
def display(data):
    for i in range(len(data)):
        print(data[i][0])


#function to create process to buy laptop and update txx file after laptop is bought
def buy(Customer_name):
    filedata = file_data("laptop.txt.txt")
    data = data_list(filedata)

    for i in range(len(data)):
        for j in range(2,4):
            data[i][j] = int(data[i][j])

    print("laptop list:")
    print("{:<10}{:<25}{:<21}{:<19}{:<14}{:<23}{:<15}".format("S.No", "Name of the Laptop", "Laptop Brand", "Price", "Quantity", "Processor Details", "Graphic Card"))
    for i, row in enumerate(data, start=1):
        laptop_name, laptop_brand, price_laptop, quantity, processor, graphics_card = row
        print("{:<10}{:<25}{:<21}{:<19}{:<14}{:<23}{:<15}".format(i, laptop_name, laptop_brand, price_laptop, quantity, processor, graphics_card))
    print("")

    buy = {}

    from datetime import datetime
    Buy_Date = datetime.now()
    Buy_Date_str = Buy_Date.strftime("%Y-%m-%d")
    Buy_time_str = Buy_Date.strftime( "%H:%M:%S")

    buy["Name"] = Customer_name
    buy["Date bought"] = Buy_Date_str
    buy["Time Bought"] = Buy_time_str
    
    count = 0
    while count == 0:
        try:
            numberOflaptop = int(input("Number of laptops to be bought: "))
            if numberOflaptop>0:
                count = 1
            elif numberOflaptop <= 0:
                print("please enter a valid number: ")
        except:
            print("You have entered an invalid input, Please try again")
    print("")

    laptop_available = False
    total_amount = 0
    laptop = 0
    while laptop < numberOflaptop:
        nameOflaptop = input("name of the laptop: ")
        laptop+=1
        for i in range(len(data)):
            for j in range(1):
                if nameOflaptop == data[i][j] and data[i][3]>0:
                    price = data[i][2]
                    buy[data[i][0]] = price
                    total_amount += price
                    stock =data[i][3] - 1
                    data[i][3] = stock
                    laptop_available = True


    if laptop_available == False:
        print(nameOflaptop, "is not available")
        return
    
    shipping_cost = 200
    total_amount+= shipping_cost

    confirm_purchase = input(f"your total amount is {total_amount} including Shipping cost.Do you want to continue and purchase the laptop? (yes/no):")
    if confirm_purchase.lower()=="no":
        print("your order has been cancelled")
        return
    
    buy["Shipping Cost"]=200
    buy["Total Amount"]= total_amount

    import os
    transaction_ID = f"{Customer_name}_1"
    while os.path.exists((f"Transaction{transaction_ID}.txt")):
        transaction_ID_parts = transaction_ID.split("_")
        current_number = int(transaction_ID_parts[-1])
        new_number = current_number+ 1
        transaction_ID_parts[-1] = str(new_number)
        transaction_ID = "_".join(transaction_ID_parts)
    buy["Transaction ID"] = transaction_ID

    order_bill(transaction_ID,data,laptop_available,nameOflaptop,buy) # calling the order bill function from write python file

    print("\n Thank you For purchasing your laptiop from our store")
    



# function to perform the selling process and update stock after selling laptop to the shop
def sell(Seller_name):
    filedata = file_data("laptop.txt.txt")
    data = data_list(filedata)

    for i in range(len(data)):
        for j in range(2,4):
            data[i][j] = int(data[i][j])

    print("laptop list:")
    print("{:<10}{:<25}{:<21}{:<19}{:<14}{:<23}{:<15}".format("S.No", "Name of the Laptop", "Laptop Brand", "Price", "Quantity", "Processor Details", "Graphic Card"))
    for i, row in enumerate(data, start=1):
        laptop_name, laptop_brand, price_laptop, quantity, processor, graphics_card = row
        print("{:<10}{:<25}{:<21}{:<19}{:<14}{:<23}{:<15}".format(i, laptop_name, laptop_brand, price_laptop, quantity, processor, graphics_card))
    print("")

    sell = {}

    from datetime import datetime
    Sell_Date = datetime.now()
    Sell_Date_str = Sell_Date.strftime("%Y-%m-%d ")
    Sell_time_str = Sell_Date.strftime( "%H:%M:%S")

    sell["Seller/Company Name"] = Seller_name
    sell["Date Sold"] = Sell_Date_str
    sell["time Sold"] = Sell_time_str

    count =  0
    while count == 0:
        try:
            numberOflaptop = int(input("Number of laptops to be Sold: "))
            if numberOflaptop>0:
                count = 1
            elif numberOflaptop <= 0:
                print("please enter a valid number: ")
        except:
            print("You have entered an invalid input, Please try again")
    print("")

    laptop_available = False
    total_amount = 0
    laptop = 0
    while laptop < numberOflaptop:
        nameOflaptop = input("Please enter the name of the laptop: ")
        laptop+=1
        for i in range(len(data)):
            for j in range(1):
                if nameOflaptop == data[i][j] and data[i][3]>0:
                    price = data[i][2]
                    sell[data[i][0]] = price
                    total_amount += price
                    stock = data[i][3]+1
                    data[i][3] = stock
                    laptop_available = True

    if laptop_available == False:
        print(nameOflaptop, "is not available")
        return

    VAT_Amount = (13/100)*total_amount
    total_amount+=VAT_Amount

    confirm_sale = input(f"your total amount is {total_amount} including 13% VAT amount.Do you want to continue and purchase the laptop? (yes/no):")
    if confirm_sale.lower()=="no":
        print("your order has been cancelled")
        return
    
    sell["VAT Amount"] = (13/100)*total_amount
    sell["Total Amount"] = total_amount

    import os
    transaction_ID = f"{Seller_name}_1"
    while os.path.exists((f"Transaction{transaction_ID}.txt")):
        transaction_ID_parts = transaction_ID.split("_")
        current_number = int(transaction_ID_parts[-1])
        new_number = current_number+ 1
        transaction_ID_parts[-1] = str(new_number)
        transaction_ID = "_".join(transaction_ID_parts)
    sell["Transaction ID"] = transaction_ID


    sell_bill(transaction_ID,data,laptop_available,nameOflaptop,sell)# calling the function of sell bill from the write pyhon file.

    print("\n Thank you For selling laptiop to our store")

   