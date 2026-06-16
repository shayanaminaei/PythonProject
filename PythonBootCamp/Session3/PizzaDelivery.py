print("Welcome to the Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, L: ").lower()
add_pepperoni = input("Do you want pepperoni? (y/n): ").lower()
extra_cheese = input("Do you want extra cheese? (y/n): ").lower()

bill = 0

if size == "s":
    bill += 15

elif size == "m":
    bill += 20

elif size == "l":
    bill += 25


if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3


if extra_cheese == "y":
    bill += 1


print(f"You'r inputs are : {size},{add_pepperoni},{extra_cheese}\n"
      f"Your final bill is ${bill}.")