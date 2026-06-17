# find input number_input is odd or even
number = int(input("Which number_input do you want to check? "))
if number % 2 == 0:
    print(f"the  number_input that you said ({number}) is Even")

if number % 2 != 0:
    print(f"the  number_input that you said ({number}) is Odd")


print("exiting...")