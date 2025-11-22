print("Wellcome to Python Pizza Delivery")
size = input("What size of Pizza do you want ? S , M , L : ")
pepperonal = input("Do you want pepperonal on your pizza ? Y or N : ")
extra_cheese = input("D you want extra cheese ? Y or N : ")
totalBill = 0
if size == "S":
    totalBill += 5
    
    print(f"your Bill is {totalBill}")
elif size =="M":
    totalBill += 20
    
    print(f"your Bill is {totalBill}")
elif size == "L":
    totalBill +=25
    if pepperonal == "Y":
        totalBill += 3
    if extra_cheese == "Y":
        totalBill += 1
    print(f"your Bill is {totalBill}")  
else :
    print("You type wrong input !")


if pepperonal == "Y":
        if size == "S":
            totalBill += 2
        else:
             totalBill += 3

if extra_cheese == "Y":
    totalBill += 1

print(f"your total bill is {totalBill}")

