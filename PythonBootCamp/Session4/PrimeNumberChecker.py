banner = """
██████  ██████  ██ ███    ███ ███████     ███    ██ ██    ██ ███    ███ ██████  ███████ ██████       ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
██   ██ ██   ██ ██ ████  ████ ██          ████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██     ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
██████  ██████  ██ ██ ████ ██ █████       ██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████      ██      ███████ █████   ██      █████   █████   ██████  
██      ██   ██ ██ ██  ██  ██ ██          ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██     ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
██      ██   ██ ██ ██      ██ ███████     ██   ████  ██████  ██      ██ ██████  ███████ ██   ██      ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
"""
print(banner)
number_input = int( input( "Enter a number_input: " ) )
continue_checking = True
def number_checker(number):
    prime = True
    divide_numbers = [2, 3, 5, 7, 9, 11]
    for numbers in divide_numbers:

        if number % numbers == 0 and number_input != numbers:
            prime = False
            break

    if prime:
        print("The number_input is prime")

    else:
        print("The number_input is not prime")

while continue_checking:
    number_checker( number_input )
    answer = input("Do you want to continue? (y/n) ").lower()

    if answer == "n":
        print("Exiting...")
        continue_checking = False
    elif answer == "y":
        print("Continuing...")
        number_input = int( input( "Enter a number_input: " ) )