import random

print("Welcome to Password Generator!")
letters = [
    'a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u','v',
    'w','x','y','z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*']
password_length = int(input("Enter the password length: "))


# check loop for inputs
while True:

    symbol_count = int(input("Enter the number_input of symbols: "))
    number_count = int(input("Enter the number_input of numbers: "))

    if symbol_count + number_count <= password_length:
        break

    else:
        print(
            f"Error! Your password length is {password_length}, "
            f"but symbols + numbers = {symbol_count + number_count}"
        )
        print("Try again...\n")

password_list = []

# remaining characters become letters
letter_count = password_length - symbol_count - number_count

# add letters
for char in range(letter_count):
    password_list.append(random.choice(letters))

# add symbols
for char in range(symbol_count):
    password_list.append(random.choice(symbols))

# add numbers
for char in range(number_count):
    password_list.append(random.choice(numbers))

print("Before shuffle:")
print(password_list)

random.shuffle(password_list)

print("After shuffle:")
print(password_list)

password = ""

for char in password_list:
    password += char

print("Your password is:", password)