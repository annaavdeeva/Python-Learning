# Practice questions for CLASSES

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''

class BankAccount (object):

    status = "Anya's bank client"
    
    def __init__(self, name, balance=0.0):
        self.balance = balance
        self.name = name
    
    def display_balance(self):
        print(f'Hi {self.name}! Your account balance is: ${self.balance}')

    def deposit(self):
        amount = float(input("How much money would you like to deposit? >>> "))
        self.balance += amount
        print(f'Balance is now ${self.balance}')
       
    def withdraw(self):
        amount = float(input("How much much would you like to withdraw? >>> "))
        if amount > self.balance:
            print(f'Sorry, you do not have sufficient funds. Your current balance is ${self.balance}.')
        else:
            self.balance -= amount
            print(f'Withdrawal successful. Your balance is now ${self.balance}.')


'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''

import math

class Cirle(object):
    
    def __init__(self, radius):
        self.radius = radius
    
    def calc_area (self):
        area = math.pi * (self.radius)**2
        return area      
    
    
    
    
    