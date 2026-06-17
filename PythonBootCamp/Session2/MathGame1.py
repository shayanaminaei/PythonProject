# User input 2digit number_input, app should add them & show the result
#it should be able to check input multiple times
number = ""
def numberInput(string):
    number = int ( input ( "Enter 2 digit number_input: " ) )
    if 9 < number < 100 :
        lnumber = number // 10
        rnumber = number % 10
        print ( f"Number was: {number}" )
        print ( f"Left number_input: {lnumber}" )
        print ( f"Right number_input: {rnumber}" )

    else:
        print ( "Invalid input, try again..." )
        number = int ( input ( "Enter 2 digit number_input: " ) )
        numberInput(number)


numberInput( number )