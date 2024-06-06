
# function created that takes a file name as input and returns contents of the filas as a list of strings 
def file_data(file_name):
    file = open(file_name, "r")
    data = file.readlines()
    file.close()
    return data



#this ffunction converts the contents of a text file into a list of lists that can be manipulated in a program
def data_list(file):
    data = []
    for each in file:
        data.append(each.replace("\n","").split(","))
    return data
