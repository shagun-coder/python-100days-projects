print("wellcome to tip calculator")
bill = float(input("what was your total bill = $" ))
tip = int(input("How much tip you liketo give ? 10,12, or 15 ? "))


people= int(input("How many people to split the bill ? "))
bill_with_Tip = tip/100*bill + bill
totalBill = bill +bill_with_Tip
bill_Per_Person = totalBill/people
final_amount = round(bill_Per_Person,2)
print(f"Each person should pay :${final_amount}")