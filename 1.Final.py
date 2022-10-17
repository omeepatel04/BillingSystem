# Input Info
import datetime
import xlsxwriter
import pandas as pd
from datetime import date
f = open("Customer_Data.txt", "a")

print("\nInput Customer Info")
CName = input("Customer Name: ")
CNumber = input("Customer Number: ")
CAddress = input("Residential City: ")
print("\nInput Details")

# Menu

Burger = 150
Coke = 40
Pizza = 250
Taco = 100
Sandwich = 200

# Defining variables to use in loop
New = "N"
A = 0
B = 0
C = 0
D = 0
E = 0
Price = 0
True1 = False
True2 = False
True3 = False
True4 = False
True5 = False
Quantity1 = 0
Quantity2 = 0
Quantity3 = 0
Quantity4 = 0
Quantity5 = 0
Total1 = 0
Total2 = 0
Total3 = 0
Total4 = 0
Total5 = 0
Name = ["", "", "", "", ""]
Rate = [0, 0, 0, 0, 0]
BQuantity = [0, 0, 0, 0, 0]
BTotal = [0, 0, 0, 0, 0]


while (New == "N"):
    Add = input("Enter the product Id: ")
    Add = int(Add)
    Quantity = input("Enter the quanity of product sold: ")
    Quantity = int(Quantity)

    if (Add == 1):
        A = (Burger * Quantity)
        print(f"Total for this product is: {A}")
        Price += A
        Total = A
        True1 = True
        Quantity1 = Quantity
        Total1 = A

    elif (Add == 2):
        B = Coke * Quantity
        print(f"Total for this product is: {B}")
        Price += B
        Total = B
        True2 = True
        Quantity2 = Quantity
        Total2 = B

    elif (Add == 3):
        C = Pizza * Quantity
        print(f"Total for this product is: {C}")
        Price += C
        Total = C
        True3 = True
        Quantity3 = Quantity
        Total3 = C

    elif (Add == 4):
        D = Taco * Quantity
        print(f"Total for this product is: {D}")
        Price += D
        Total = D
        True4 = True
        Quantity4 = Quantity
        Total4 = D

    elif (Add == 5):
        E = Sandwich * Quantity
        print(f"Total for this product is: {E}")
        Price += E
        Total = E
        True5 = True
        Quantity5 = Quantity
        Total5 = E

    else:
        print("Invalid Product Id")

    New = input("To enter a new product press N: ").upper()

    if (True1==True):
        Name[0] = "Burger"
        Rate[0] = 150
        BQuantity[0] = Quantity1
        BTotal[0] = Total1

    if (True2==True):
        Name[1] = "Coke"
        Rate[1] = 40
        BQuantity[1] = Quantity2
        BTotal[1] = Total2

    if (True3==True):
        Name[2] = "Pizza"
        Rate[2] = 250
        BQuantity[2] = Quantity3
        BTotal[2] = Total3

    if (True4==True):
        Name[3] = "Taco"
        Rate[3] = 100
        BQuantity[3] = Quantity4
        BTotal[3] = Total4
    
    if (True5==True):
        Name[4] = "Sandwich"
        Rate[4] = 200
        BQuantity[4] = Quantity5
        BTotal[4] = Total5


    if (New != "N"):
        
        # Invoice For Customer

        print("___________________________________________")
        print("\n\tXYZ Company's Maninagar Branch")
        print("")

        print(f"Bill To: {CName}")
        print(f"Contact Number: {CNumber}")
        print(f"City: {CAddress}")
        now = datetime.datetime.now()
        Pdate = date.today()
        Ptime = now.time()

        print(f"Date: {Pdate}")
        print(f"Time: {Ptime}")

        print("\n\n\t\tCustomer Invoice")
        
        print("\nProduct      Rate      Quantity      Total")
        
        if(True1==True):
            print(f"\n{Name[0]}       {Rate[0]}       {BQuantity[0]}             {BTotal[0]}")

        if(True2==True):
            print(f"{Name[1]}         {Rate[1]}        {BQuantity[1]}             {BTotal[1]}")
        
        if(True3==True):
            print(f"{Name[2]}        {Rate[2]}       {BQuantity[2]}             {BTotal[2]}")
    
        if(True4==True):
            print(f"{Name[3]}         {Rate[3]}       {BQuantity[3]}             {BTotal[3]}")
        
        if(True5==True):
            print(f"{Name[4]}     {Rate[4]}       {BQuantity[4]}             {BTotal[4]}")
        
        print(f"\nTotal Amount To Be Paid: {Price}\n")

        print("___________________________________________\n\n")



        # Invoice For RecordKeeping 

        print("___________________________________________")
        print("\n\n\t\tStore Invoice\n\n") # Heading

        print(f"Customer Name: {CName}")
        print(f"Contact Number: {CNumber}")
        print(f"Residential City: {CAddress}")

        now = datetime.datetime.now()
        Pdate = date.today()
        Ptime = now.time()

        print(f"Date: {Pdate}")
        print(f"Time: {Ptime}")

        print("\n\n\t\tProducts Sold")
        
        print("\nProduct      Rate      Quantity      Total")
        
        if(True1==True):
            print(f"\n{Name[0]}       {Rate[0]}       {BQuantity[0]}             {BTotal[0]}")

        if(True2==True):
            print(f"{Name[1]}         {Rate[1]}        {BQuantity[1]}             {BTotal[1]}")
        
        if(True3==True):
            print(f"{Name[2]}        {Rate[2]}       {BQuantity[2]}             {BTotal[2]}")
    
        if(True4==True):
            print(f"{Name[3]}         {Rate[3]}       {BQuantity[3]}             {BTotal[3]}")
        
        if(True5==True):
            print(f"{Name[4]}     {Rate[4]}       {BQuantity[4]}             {BTotal[4]}")
        
        print(f"\nTotal Amount To Be Paid: {Price}\n")

        print("___________________________________________\n\n")



# Write in a txt file

EName = (CName + "\n")
ECity = (CAddress + "\n")
ENumber = (CNumber + "\n")
EDate = (str(Pdate) + "\n")
EBurger = (str(BQuantity[0]) + "\n")
ECoke = (str(BQuantity[1]) + "\n")
EPizza = (str(BQuantity[2]) + "\n")
ETaco = (str(BQuantity[3]) + "\n")
ESandwich = (str(BQuantity[4]) + "\n")
ETotal = (str(Price) + "\n\n")
f.write(EName)
f.write(ECity)
f.write(ENumber)
f.write(EDate)
f.write(EBurger)
f.write(ECoke)
f.write(EPizza)
f.write(ETaco)
f.write(ESandwich)
f.write(ETotal)
f.close()

f = open("Customer_Data.txt", "r")

ETable = []
ETable = f.readlines()
EName = ETable[0::11]
ECity = ETable[1::11]
ENumber = ETable[2::11]
EDate = ETable[3::11]
EBurger = ETable[4::11]
ECoke = ETable[5::11]
EPizza = ETable[6::11]
ETaco = ETable[7::11]
ESandwich = ETable[8::11]
ETotal = ETable[9::11]

EList = [
EName, ECity, ENumber, EDate, EBurger, ECoke, EPizza, ETaco, ESandwich, ETotal
]

df = pd.DataFrame(EList)

df = pd.DataFrame(EList, index=["Name", "City", "Number", "Date", "Burger", "Coke", "Pizza", "Taco", "Sandwich", "Total"])
# Transpose the dataframe.
df = df.T

writer = pd.ExcelWriter('ProductSoftwareData.xlsx', engine='xlsxwriter')
df.to_excel(writer)

writer.save()
