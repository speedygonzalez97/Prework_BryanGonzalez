#Bryan Gonzalez             Python Prework Assignment

#Question 1: Write a function to print "hello_USERNAME!" USERNAME is 
#the input of the function. The first line of the code has been defined as below.

print("\nQuestion 1: ")

def hello_name(user_name):
    
    print("\nhello_" + user_name + "!\n")

hello_name("USERNAME")

#Question 2: Write a python function, first_odds that prints 
#the odd numbers from 1-100 and returns nothing

print("Question 2: \n")

def first_odds():

    i = 1
    while i < 101:
        print(i)
        i += 2
       
    return '\nnothing\n'

print(first_odds())

#Question 3: Please write a Python function, max_num_in_list to return 
#the max number of a given list. The first line of the code has been defined as below.

print("Question 3: \n")

def max_num_in_list(a_list):

    a_list = [34,92,32,39,19,53,65,3,66,89]
    print(max(a_list))

max_num_in_list("max number")

#Question 4: Write a function to return if the given year is a leap year. 
#A leap year is divisible by 4, but not divisible by 100, unless it is also divisible 
#by 400. The return should be boolean Type (true/false).

print("\nQuestion 4: \n")

def is_leap_year(a_year):
    print("\n")
    if a_year % 4 == 0:
        if a_year % 100 != 0 or a_year % 400 == 0:
            print(bool(True))
        else:
            print(bool(False))
    else:
        print(bool(False))
x = int(input("\nDetermine if given year is a leap year: "))

is_leap_year(x)

#Question 5: Write a function to check to see if all numbers in list are consecutive
#numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not 
#consecutive numbers. The return should be boolean Type.

print("\nQuestion 5: \n")

def is_consecutive(a_list): 
   print("\n")
   x = min(a_list) 
   y = max(a_list)
   if y - x + 1 == len(a_list): 
        for n in range(len(a_list)): 
            if a_list[n] < 0: 
                m = -a_list[n] - x
            else: 
                m = a_list[n] - x
            if a_list[m] > 0: 
                a_list[m] = -a_list[m] 
            else: 
                return False 
        return True 
   return False

list = [14,19,18,17,15,16]
print(is_consecutive(list))
print("\n")
