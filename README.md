# passwordGenerator.py
#### Video Demo: <https://youtu.be/IlKUXL_QN-E>
#### Description:

The main function first asks the user how many passwords they would like to create. 
It takes input from the user and allows them to create a password of either all letters A-Za-z or a combination of letters, numbers, and special symbols.
The user is also prompted about their desired length of password, as long as it is at least 5 characters.

The if statement executes in main if the user inputs that they want a password with only characters A-Za-z. 
The function password_only_chars is used to randomly generate characters individually, and add them to an initially empty string in the desired length of 
the password. Each time a password is   finished it is returned to the password_only_chars function and returned to the if statement in main. 
Main then passes the each password indivitually to the function csv_domain_and_pw where the user is prompted as many times as the number of passwords 
they want the program to create, to enter a Domain  name. This function then writes the Domain name and corresponding random password to a CVS file.

The else statement in main executes if the user wants passwords that contain letters A-Za-z, numbers, and special characters. 
The number of passwords is used in a for loop such that every time the function password_final runs, until the number of passwords the user wants 
is created, the function will continue to run and individually create passwords that then get passed to csv_domain_and_pw to be printed to a CSV file 
along with the corresponding domains.

The function final_passwords takes an input of the amount of numbers, special symbols, and characters A-Za-z the user wants in their password. 
Subtracting the number of characters from the amount of numbers plus special symbols tells how many characters should be in the password created such 
that it is the desired length. an empty password string is created and for loops are used to add the random characters,symbols, and numbers to the 
string until it is has #the desired amount of each character. The characters are then shuffled and returned to the else function in main.
    
The function check_num_passwords will continue to prompt the user asking how many passwords they would like to be created until they enter a value 
greater than 0. If the user writes out the number instead of giving the digit, for example "three" instead of "3", the w2n function from the 
word2number file converts the written word to the integer. I originally wanted to ask the all of the questions in the main file, but found 
it impossible to do so while also #being able to continue to reprompt the user until they enter valid output. That is why I ended up putting 
all of the questions in their own function so i #could enable re-prompting thorugh use of the while loop.
    
The function check_pw_is_valid_length will continue to reprompt the user until they enter a length greater than the minimum requirement of 5 characters. 
It also uses the w2n function from the word2number library to convert written numbers to the corresponding integer, for example "six" to the integer "6".
The #program overall could be improved by asking the user for the minimum about of characters they want in addition to the maximum. 
I hardcoded a minimum of 5 characters since I knew that figuring out how to actually generate and combine random integers would be the most difficult
and time consuming part of this project.
    
The function check_is_valid_numbers continues to reprompt the user until they enter a value greater than zero, and also uses w2n to change any written 
words to the corresponding integer. It also ensures that the value entered by the user will not result in a password that is greater in length than the 
original desired length. The user will continue to be reprompted until they enter a value that does not exceed the overall desired password length the 
user initially indicated.
        
The function check_is_valid_symbols continues to reprompt the user until they enter a value greater than zero, and also uses w2n to change any written 
words to the corresponding integer. It also ensures that the value entered by the user will not result in a password that is greater in length than the 
original desired length. The user will continue to be reprompted until they enter a value that does not exceed the overall desired password length the 
user initially indicated.
            
The csv_domain_and_pw(password) function will run each time a password is created. The user will continually be prompted to enter a domain name, like 
facebook, instagram etc, until they have entered as many names as the amount of passwords they wanted the program to create. After the last entry the 
program ends. All of the domains and passwords are written to the domain_password.csv file. There are three big improvements than can be made to this 
section #of code. One is to change it so that the head Domain : Password only prints once at the top instead of before each new entry. Two, by 
implementing the use of sys.argv and command line arguments, the user can be asked to enter the domain names, with spaces between each name, all at 
once and hit enter. The code would then prompt the user if they entered too many or too little names based on the amount of passwords they wanted 
created. Otherwise it would write the names to the csv file. this owuld make the program shorter, less repetitive when run, and more user friendly. 
I did not do this bc I did not think of it until after I finished the code, but would implement this in the future to improve this code. The third and 
final improvement is that domain names currently can be repeated in the csv file editing the code so it would tell the user that a password for the 
name entered and that they cannot have duplicate domain names would further improve the program.
