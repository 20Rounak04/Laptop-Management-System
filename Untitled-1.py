value = int(input("Please enter a number: "))

def value_divisible(value):
    
    if (value%3==0):
        print("The value is divisible by 3")
       
    else:
        print("The value is not divisible by 3")

value_divisible(value)