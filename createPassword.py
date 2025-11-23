import random
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
number_series = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_series = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Wellcome to the pyPassword Generator")
num = int(input("How many letter would you want to add in your password : "))
symbol = int(input("How many symbol would you like in your password : "))
number = int(input("How many numbers would you like : "))
get_password_list = []
for char in range(1, num + 1):
 
    get_password_list.append(random.choice(letters))
for sym in range(1, symbol + 1):
    get_password_list.append(random.choice(symbols_series))
for num in range(1, number + 1):
    get_password_list.append(random.choice(number_series))

random.shuffle(get_password_list)
password = ""
for char in get_password_list:
    password += char
print(f"Your password is : {password}")


