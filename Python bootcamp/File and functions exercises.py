# Practice questions for FILES AND FUNCTIONS


'''
Question 1
Create a function that will calculate the sum of two numbers. Call it sum_two.
'''

# returns a sum of two numbers, if one of the numbers is not specified,
# defaults to zero

def sum_two(num1=0, num2=0):
    print(f'The sum of {num1} and {num2} is {num1+num2}')

sum_two(120,785)



'''
Question 2
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.
'''

# returns a product of two numbers, if second value not specified, multiplied
# by two as default

def multiply_two(a=0,b=2):
    print(f'The product of {a} and {b} is {a*b}')

multiply_two(5)
multiply_two(12,67)
multiply_two()



'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''

# a function that raises a number to the power of another number, if not 
# specified, f is defaulted to 2

def exponent(i=0,f=2):
    print(f'{i} to the power of {f} is {i**f}')

exponent(5,3)
exponent(5)
exponent()



'''
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.
'''

f = open("capitals.txt","w")
f.write("London, ")
f.write("Amsterdam, ")
f.write("Minsk, ")
f.write("Adu Dhabi, ")
f.write("Paris")
f.close()



'''
Question 5
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.
'''

new_capital = input("Please enter a capital city: >>> ")

f = open("capitals.txt", "a")
f.write(", "+ new_capital)
f.close()

f = open("capitals.txt", "r")
print(f.read())
f.close()



'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''

# copies a specified file_in into a copy of that file file_out

def copy_file(file_in, file_out):
    with open(file_in) as file1:
        with open(file_out, "w") as file2:
            file2.write(file1.read())
        
copy_file("capitals.txt","copy_capitals.txt")



