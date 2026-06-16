# find input number is odd or even
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print(f"the  number that you said ({number}) is Even")

if number % 2 != 0:
    print(f"the  number that you said ({number}) is Odd")


print("exiting...")