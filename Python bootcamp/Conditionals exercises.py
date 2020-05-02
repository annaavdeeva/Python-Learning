# Practice questions for CONDITIONALS

'''
Question 1: Write code that asks the user to input a number between 1 and 5
inclusive. The code will take the integer and print out the string value. So
for example, if the user inputs 2, the code will print two. Reject any input
that is not a number in that range
'''

input_number = int(input("Please input a number between 1 and 5: >>> "))
if input_number == 1:
    print ("one")
elif input_number == 2:
    print ("two")
elif input_number == 3:
    print ("three")
elif input_number == 4:
    print ("four")
elif input_number == 5:
    print ("five")
else:
    print("That is not a number between 1 and 5, silly!")



'''
Question 2: Repeat the previous task but this time the user will input a
string and the code will output the integer value. Convert the string to
lowercase first
'''

input_text = input("Please specify a string between One and Five: >>> ")
input_text = input_text.lower()
if input_text == "one":
    print(int(1))
elif input_text == "two":
    print(int(2))
elif input_text == "three":
    print(int(3))
elif input_text == "four":
    print(int(4))
elif input_text == "five":
    print(int(5))
else:
    print("Out of scope.")



'''
Question 3: Create a variable containing an integer between 1 and 10 inclusive.
Ask the user to guess the number. If they guess too high or too low, tell
them they have not won. Tell them they will win if they guess the correct
number.
'''

secret_number = 4
guess_number = input("Guess a number between 1 and 10: >>> ")
if guess_number.isdigit():
    guess_number = int(guess_number)
    if guess_number == secret_number:
        print ("Yes, that's correct! YOU WIN.")
    elif guess_number < secret_number and guess_number >= 1:
        print ("Number is too low! YOU LOSE.")
    elif guess_number > secret_number and guess_number <= 10:
        print ("Number is too high! YOU LOSE.")
    else:
        print ("Out of scope.")
else:
    print("That's not a number, silly!")
    
    
    
'''
Question 4: Ask the user to input their name. Check the length of the name.
If it is greater than 5 characters long, write a message telling them how
many characters, otherwise write a message saying the length of their name
is a secret
'''

input_name = input("Put your name here and I will tell you the length: >>> ")
length_name = len(input_name)
if length_name > 5:
    print(length_name)
else:
    print ("The length of your name is a secret")



'''
Question 5: Ask the user for two integers between 1 and 20. If they are both
greater than 15 return their product. If only one is greater than 15 then
return their sum, if neither are greater than 15 return zero
'''

int_1 = int(input("Please enter an integer between 1 and 20: >>> "))
int_2 = int(input("PLease enter another integer between 1 and 20: >>> "))
int_product = int_1*int_2
int_sum = int_1+int_2
if int_1 > 15 and int_2 > 15:
    print ("The product of", int_1, "and", int_2, "is", int_product)
elif int_1 > 15 or int_2 > 15:
    print ("The sum of", int_1, "and", int_2, "is", int_sum)
else:
    print(0)



'''
Question 6: Ask the user for two integers, then swap the contents of the
variables. So if var_1 = 1 and var_2 = 2 initially, once the code has run
var_1 shoud equal to 2 and var_2 should equal to 1.
'''

var_1 = int(input("Please enter an integer: >>> "))
var_2 = int(input("Please enter another integer: >>> "))
print ("Before swapping: first integer was", var_1, "and second integer was",
       var_2)
var_1,var_2 = (var_2, var_1)
print ("After swapping: the first integer is now", var_1, "and second is now",
       var_2)


