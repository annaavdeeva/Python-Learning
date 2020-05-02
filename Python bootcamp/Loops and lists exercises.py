c

'''
Question 1: Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results
'''

# input prompt to enter two numbers
num_1 = int(input("Please enter number between 1 and 100: >>> "))
num_2 = int(input("Please enter second number between 1 and 100: >>> "))

# a while loop that will not let the user enter numbers that are less than 0
# more than 100 or numbers that are equal to each other
while num_1 <= 0 or num_2 <= 0 or num_1 > 100 or num_2 > 100 or num_1 == num_2:
    print("Values must be different and between 1 and 100. Please try again.")
    num_1 = int(input("Please enter number between 1 and 100: >>> "))
    num_2 = int(input("Please enter second number between 1 and 100: >>> "))
 
# if statements that allow to check for which number is smaller to print the
# numbers in the range from smallest to biggest
if num_1<num_2:
    for i in range(num_1,num_2+1):
        print(i, end = " ")
if num_2<num_1:
    for i in range(num_2, num_1+1):
        print(i, end = " ")
        


'''
Question 2: Ask the user to input a string and then print it out to the screen
in reverse order (use a for loop).
'''

# input prompt to enter a string
user_string = input("Please enter and string and I will reverse it:\n>>> ")

# creating an empty variable that will act as the new string
reverse_string = " "

# loop that adds the empty string to each character (order is important)
for char in user_string:
    reverse_string = char + reverse_string
print(reverse_string, end = "")

# can also do it in this way which is shorter:

user_string = input("Please enter and string and I will reverse it:\n>>> ")
print(user_string[::-1])



'''
Question 3: Ask the user for a number between 1 and 12 and then display
a times table for that number.
'''

# input prompt which asks the user to enter a number between 1 and 12
num = input("Please enter a number between 1 and 12 to see times table: ")

# while loop that checks if the number is a string, or not in range
while (not num.isdigit() or (int(num)) < 1 or (int(num)) > 12):
    print("Please enter an integer between 1 and 12. Try again")
    input("Please enter a number between 1 and 12 to see times table: ")

# formatting for the table
num=int(num) 
print("=====================")
print(f'Times table for {num}')
print("=====================")
# for loop that multiplies the entered number by the range of numbers
for i in range(1,13):
    print(f'{i} x {num} = {i*num}')
print("=====================")
        


'''
Question 4: Can you amend the solution to question 3 so that it just prints
out a times table between 1 and 12? (No need to ask for user input)
'''

# nested loop that multiplies two ranges by each other
for i in range(1,13):
    print("=====================")
    print(f'This is the {i} times table')
    print("=====================")
    for j in range(1,13):
        print(f'{j} x {i} = {j*i}')



'''
Question 5: Ask the user to input a sequence of numbers. The calculate the mean 
and print the result.
'''

# input prompt
user_number = input("Please input a number, type exit to stop: >>> ")
# creating an empty set for numbers which the user will enter
numbers = []

# a while loop that allows the user to type exit to leave the prompt
while user_number.lower() != "exit":

# a while loop that checks that the input is digits only
    while (not user_number.isdigit()):
        print ("Please enter integers only")
        user_number = input("Please input a number: >>> ")

# adding the input numbers onto the numbers set
    numbers.append(int(user_number))
    print(f'{user_number} has been added')
    user_number = input("Next number please: >>> ")

# creating a running total
total = 0
for j in numbers:
    total += j

# calculating the mean
print(f'The mean of {user_number} is {total/len(numbers)}')
print(sum(numbers)/len(numbers))



'''
Question 6: Write code that will calculate 15 factorial.
'''

n = 3
fact = 1
for i in range(1,n+1):
    fact = fact * i

print(fact)



'''
Question 7: Write code to calculate Fibonacci numbers. Create a list containing
the first 20 Fibonacci numbers (made by sum of the preceding two values).
'''
# number of Fibonacci numbers required
n = 20

# the first two numbers in the sequence are 0 and 1
a = 0
b = 1

# creating an empty set that will append numbers into it
fib_nums = []

# a loop that will create the Fibonacci sequence and loop it n times
for i in range(n):
    fib_nums.append(a)
    a,b = b,a+b

print (f'The first {n} Fibonacci numbers:{fib_nums}')



'''
Question 8: Write code that will determine all odd and even numbers between
1 and 100. Put the odds in a list named odd and evens in a list named even
'''

# numbers required
n = 100

# create empty sets for odd and even
odd = []
even = []

for i in range(n+1):
    if not i % 2:
        even.append(i)
    else:
        odd.append(i)

print("The odds are ", odd)
print("The evens are", even)

