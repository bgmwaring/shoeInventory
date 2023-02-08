#=====Import libaries=====
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity =quantity
        
    def get_cost(self):
        return(self.cost)

    def get_quantity(self):
        return(self.quantity)

    def __repr__(self):
        return(f"[{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}]\n")

#=============Shoe list===========
# establish storage variable for inventory
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():

    with open("inventory.txt", "r") as f:
        
        lines = f.readlines()
        lines = lines[1:]
        
        for line in lines:
            shoe = line.strip("\n")
            shoe = shoe.split(",")
            
            shoe_list.append(Shoe(shoe[0], shoe[1], shoe[2], shoe[3], shoe[4]))

def capture_shoes():
    
    shoe_list.append(Shoe(input("Enter country: "),
                          input("Enter code: "),
                          input("Enter product: "),
                          input("Enter cost: "),
                          input("Enter quantity: ")))
    
def view_all():
    print(tabulate(shoe_list))

def re_stock():

    # establish variables 
    index = 0
    lowest_quantity = 1000000
    
    for i in range(0, len(shoe_list)):
        shoe = shoe_list[i]
        # check quatity of shoe 
        if int(shoe[4]) < lowest_quantity:
            index = i
            lowest_quantity = int(shoe[4])
    
    # request user amount for re-stock
    amount = int(input("Re-stock amount: "))
    
    # adjust shoe list
    amount += lowest_quantity
    shoe_list[index, 4] = str(amount)
    
def search_shoe():
    
    # request shoe code from user
    code = input("Enter shoe code: ")
    
    # search shoe list for code
    for i in range(0, len(shoe_list)):
        if shoe_list[i, 1] == code:
            print(shoe_list[i])

def value_per_item():
    
    # establish storage variable for costs
    costs= []
    
    # compute and store costs for each shoe
    for i in range(0, len(shoe_list)):
        cost = int(shoe_list[i, 3]) * int(shoe_list[i, 4])
        costs.append(cost)
        
    # print data
    for i in range(0, len(shoe_list)):
        print(f"Value of {shoe_list[i, 1]} is {costs[i]}.")
        
def highest_qty():
    
    # establish variables 
    index = 0
    highest_quantity = 0
    
    for i in range(0, len(shoe_list)):
        shoe = shoe_list[i]
        # check quatity of shoe 
        if int(shoe[4]) > highest_quantity:
            index = i
            highest_quantity = int(shoe[4])
            
    print(f"{shoe_list[index]} is for sale.")
    
#==========Main Menu=============
# read data from text file first
read_shoes_data()

while True:
    
    menu = input('''Select one of the following option below:
                    cs - Capture shoe
                    va - View all
                    rs - Re-stock
                    s - Search
                    v - Value per item
                    hq - Highest quantity
                    q - Quit
                    : ''').lower()
    
    if menu == "cs":
        capture_shoes()
    elif menu == "va":
        view_all()
    elif menu == "rs":
        re_stock()
    elif menu == "s":
        search_shoe()
    elif menu == "v":
        value_per_item()
    elif menu == "hq":
        highest_qty()
    elif menu == "q":
        quit()
    else:
        print("Please select one of the given options.")
        
                