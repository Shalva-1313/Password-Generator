import random
import string
from word2number import w2n
import csv

### create video and then done!

def main():
    print("\nWelcome to your password generator.\n All passwords created will be saved in the PasswordList.csv file.")
    print("Password length must be at least 5 characters.")
    print("Symbols and numbers are optional, but highly recommended to create a strong password. \n")
    amount_passwords = check_num_passwords()
    number_letters = check_pw_is_valid_length()
    number_numbers = check_is_valid_numbers(number_letters)
    number_symbols = check_is_valid_symbols(number_numbers, number_letters)

    #executes only if user wants password(s) with characters (A-Za-z) only
    if number_numbers == 0 and number_symbols == 0:
        for i in range(amount_passwords):
            #domain = domain_for_password(amount_passwords) #writes domain to first column of csv file
            password = (password_only_chars(number_letters))
            csv_domain_and_pw(password)

    #runs method final_password to create password(s) for all other cases.
    else:
        for i in range(amount_passwords):
            password = final_password(number_letters, number_numbers, number_symbols)
            csv_domain_and_pw(password)

#check that number of passwords is greater than 0
def check_num_passwords():
    while True:
        try:
            #continue to prompt user until they give value of 5 or greater
            amount_passwords = int(input("How many passwords should be created? "))

            #checks if the user wrote "one" instead of "1", and converts "one" to "1".
            if int(amount_passwords) == False:
                amount_passwords = w2n.word_to_num(amount_passwords)
                return amount_passwords
            if int(amount_passwords) < 1:
                print("Amount of passwords must at least be 1.")
                continue
            else:
                return amount_passwords
        #if an int like eight was entered by the user instead of 8
        except ValueError:
            print("Please enter an integer greater than 0.")
            continue

#check that password will be at least 5 letters
def check_pw_is_valid_length():
    while True:
        try:
            #continue to prompt user until they give value of 5 or greater
            number_letters = input("What should the password length be? ")

            #checks if the user wrote the integer out like "one" instead of 1.
            #code works based on user input being an interger.
            if int(number_letters) == False:
                number_letters = w2n.word_to_num(number_letters)

            if int(number_letters) < 5:
                print("Input of characters must be at least 5.")
                continue
            else:
                return int(number_letters)
        #if an int like eight was entered instead of 8
        except ValueError:
            print("Please enter an integer of at least 5")
            continue

#check that number of numbers is a non-negative number
def check_is_valid_numbers(num_let):
    while True:
        try:
            #continue to prompt user until they give value of 0 or greater
            number_numbers = (input("How many numbers should the password contain? "))

            #checks if the user wrote the integer out like "one" instead of 1.
            #code works based on user input being an interger.
            if int(number_numbers) == False:
                number_numbers = w2n.word_to_num(number_numbers)

            if int(number_numbers) < 0:
                print("Input of letters must be at least 5.")
                continue
            elif int(number_numbers) > num_let:
                print("Amount cannot be greater than the desired length of the password. Re-enter an appropriate amount.")
            elif int(number_numbers) == 0:
                return int(number_numbers)
            else:
                return int(number_numbers)
        #if an int like zero was entered instead of 0
        except EOFError:
            print("Please enter a non-negative integer")
            continue

#check that number of symbols is a non-negative number
def check_is_valid_symbols(num_num, num_let):
    while True:
        try:
            #continue to prompt user until they give value of 0 or greater
            number_symbols = input("How many symbols should the password contain? ")

            #checks if the user wrote the integer out like "one" instead of 1.
            #code works based on user input being an interger.
            if int(number_symbols) == False:
                number_symbols = w2n.word_to_num(number_symbols)

            if int(number_symbols) < 0:
                print("Input cannot be a negative number.")
                continue
            elif int(number_symbols) > ((num_let)-(num_num)):
                print("Number of Symbols cannot exceed desired password length. Re-enter an appropriate amount")
            elif number_symbols == 0:
                return int(number_symbols)
            else:
                return int(number_symbols)
        #if an int like zero was entered instead of 0
        except EOFError:
            print("Please enter a non-negative integer")
            continue

def password_only_chars(num_let):
    # With combination of lower and upper case
    length = int(num_let)
    result_str = ''.join((random.choice(string.ascii_letters)) for i in range(length))
    return(result_str)

def final_password(a, b, c):
    finallength = (a-(b+c))
    password = ''
    #print letters to make up full length of pw
    for i in range(finallength):
        password += random.choice(string.ascii_letters)
    # select b digits
    for i in range(b):
        password += random.choice(string.digits)
    # select c special symbol
    for i in range(c):
        password += random.choice(string.punctuation)
    # shuffle all characters
    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

def csv_domain_and_pw(password):
    domain = input(f"Enter a domain name: ")
    #makes domain name uppercase so it looks neater in CSV file
    domain = domain.upper()
    with open("PasswordList.csv", "a") as newfile:     #a = append mode so you keep adding not replacing
        csv_writer = csv.DictWriter(newfile, fieldnames=["Domain", "Password"], delimiter = "\t") # list of column names in file
        csv_writer.writeheader()
        csv_writer.writerow({"Domain":domain, "Password":password})

if __name__ == "__main__":
    main()
