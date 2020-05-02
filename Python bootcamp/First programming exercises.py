# program to calculate an area of a circle when radius is the input

pi = 3.14159
radius = float(input("Write radius of your circle to find area.\n\tRadius here: "))
area = (radius**2)*pi
print("You entered:", radius, "Area is:", area)

# program to convert fahrenheit to celcius

fahrenheit = float(input("Enter the temperature in Fahrenheit here: "))
celcius = (fahrenheit-32)*(5/9)
print ("Celcius: ", celcius)

# program to obtain a sum of two integers

s_num1 = int(input("Write first value here: "))
s_num2 = int(input("Write second value here: "))
sum_of_num = print("The sum of " + str(s_num1) + " and " + str(s_num2) + 
                   " is " + str(s_num1+s_num2))

# program to obtain a product of two integers

p_num1 = int(input("Write first value here: "))
p_num2 = int(input("Write second value here: "))
product = p_num1*p_num2
product_of_num = print("The product of", p_num1, "and", p_num2, "is", product)

# program to determine the minimum number of pizzas to order (pizza size 6 slices)

num_people = int(input("Enter number of people ordering pizza: "))
num_slices = int(input("Now enter the number of slices each person will have: "))
total_slices = num_people * num_slices
pizza_size = 8
num_pizzas = total_slices//pizza_size
remainder_slices = (num_pizzas*(pizza_size)-total_slices)
print("You will need a minimum of", abs(num_pizzas), "of pizzas.",
      "There will be", remainder_slices, "slices left.")