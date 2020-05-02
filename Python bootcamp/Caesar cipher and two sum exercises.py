# Practice questions for ADVANCED PYTHON: CAESAR AND TWO SUM

'''
Problem 1: Create a Caesar cipher that will encrypt and decrypt messages
'''

# shift_amount makes sure to take the loop back to the beginning of the key
# if the letter passes the end of the alphabet
def shift_amount(i):
    return i%26

def encrypt(text,code):
    key = ("abcdefghijklmnopqrstuvwxyz")
    encrypted_message = " "
    text = text.lower()
    for char in text:
        if char not in key:
            encrypted_message = encrypted_message + char
        else:
            key_index = key.find(char)
            encrypted_message = encrypted_message + key[shift_amount(key_index +code)]
    return encrypted_message


code_1 = encrypt("The cat sat on the mat.",11)

    
code_2 = encrypt(code_1,-11)

print(code_1)
print(code_2)



'''
Problem 2: Two sum problem. Create a function that can take in a list and
a target value and return the indeces of the numbers that sum to the taget
'''

def two_sums(the_list, target):
    d = {}
    
    for i in range(len(the_list)):
        if target - the_list[i] in d:
            print(d)
            return [d[target-the_list[i]],i]
        d[the_list[i]]= i
    return -1

a = [1,5,7,3,4]

print(two_sums(a,9))



'''
Problem 3: Create an object that's a class that creates a playing card
'''

class Card(object):
    
    def __init__ (self, value, suit):
        self.value = value
        self.suit = suit
    
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
    
    def __str__(self):
        my_card = str(self.value) + " of " + str(self.suit)
        return my_card
    

print(Card(2,"Diamonds"))
        
        
        
        
        
        
        
        
        





