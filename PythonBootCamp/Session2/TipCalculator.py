# Tip Calculator With if-else statement

print("Welcome to tip calculator:")

TotalBill = float(input("Enter total bill: $"))
HowManyPeople = int(input("Enter how many people: "))
TipPercentage = int(input("Enter tip percentage number_input: 10 15 20 25: "))


if TipPercentage in [10, 15, 20, 25]:

    print("Calculating...")

    EachPersonBill = (
        TotalBill + (TotalBill * TipPercentage / 100)
    ) / HowManyPeople

    print(f"Each person should pay ${round(EachPersonBill, 2)}")

else:
    print("Tip percentage input was wrong. Try again.")