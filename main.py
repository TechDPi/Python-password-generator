#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:

# I creat lists of random char using random.sample() and then converted in strings using "".join()
random_letters = random.sample(letters, nr_letters)
x_random_letters = "".join(random_letters)

random_symbols = random.sample(symbols, nr_symbols)
x_random_symbols = "".join(random_symbols)

random_numbers = random.sample(numbers, nr_numbers)
x_random_numbers = "".join(random_numbers)

print(f"This is a good and strong password, but your NOT fully randomized : {x_random_letters}{x_random_symbols}{x_random_numbers}\n")

#Hard Level - Order of characters randomised:

#For fully randomise it I usude the function random.sample combined with the function len()
new_password = str(x_random_numbers) + str(x_random_symbols) + str(x_random_letters)
hard_password = ''.join(random.sample(new_password, len(new_password)))

print(f"This is your fully randomized and HARD password : {hard_password}\n")

