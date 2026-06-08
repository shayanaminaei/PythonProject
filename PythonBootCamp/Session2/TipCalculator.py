print("welcome to tip calculator: ")
#esle if in this program is rigged
TotalBill = float(input("enter total bill:$"))
HowManyPeople = int(input("enter how many people: "))
TipPercentage = int(input("enter tip percentage number: 10  15  20  25  "))
if TipPercentage == 10 or 15 or 20 or 25 :
    print("Calculating...")
    print ( "Each person should pay $" +
            str ( (TotalBill + (TipPercentage / 100)) / HowManyPeople ) )

elif TipPercentage != 10 or 15 or 20 or 25 :
    print ( "tip percentage input was wrong. try again: " )
    TipPercentage = int ( input ( "enter tip percentage: 10  15  20  25 " ) )
