
# function creates buy transaction  bill and updates laptop inventory as per the ntransaction
def order_bill(transaction_ID,data,laptop_available,nameOflaptop,buy):
    if laptop_available == True:

        file = open(f"Transaction_{transaction_ID}.txt","w")
        file.write("buy Transaction:\n")
        print("")
        print("\ntransaction details details:")
        for key, value in buy.items():
            transaction_details = key +":"+str(value)
            file.write(transaction_details)
            file.write("\n")
            print(transaction_details)
        file.close

        for i in range(len(data)):
            for j in range(2,4):
                data[i][j] = str(data[i][j])

        main_file = open("laptop.txt.txt","w")
        for items in data:
            data_update = ",".join(items)   
            main_file.write(data_update+"\n")
        main_file.close()

      
             


# function creates sell transaction  bill and updates laptop inventory as per the transaction

def sell_bill(transaction_ID,data,laptop_available,nameOflaptop,sell):
    if laptop_available == True:

       file = open(f"Transaction_{transaction_ID}.txt","w")
       file.write("Selling Transaction:\n")
       print("")
       print("\transaction details details:")
       for key, value in sell.items():
            transaction_details = key +":"+str(value)
            file.write(transaction_details)
            file.write("\n")
            print(transaction_details)
       file.close

       for i in range(len(data)):
            for j in range(2,4):
                data[i][j] = str(data[i][j])

       main_file = open("laptop.txt.txt","w")
       for items in data:
            data_update = ",".join(items)   
            main_file.write(data_update+"\n")
       main_file.close()

       
        