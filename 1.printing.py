
# 1. Using the print method, print "Hello World"
#print("Hello World")
# 2. Create variables for the data type below. 
# Data Types:
# Int
# Float
# String
# Boolean 
# Boolean (The other boolean value)
# Lists ( 4 items in list min.)
# Dictionaries  ( 4 key/value pairs min.)
int = 27
float = 3.14
string = "Howdy, Y'all"
boolean = True
boolean_other = False
list = ["summer", "Fall", "Winter", "Spring"]
dictionary = {
    "name": "Harp",
    "age": 27,
    "city": "New York",
    "country": "usa"
}


# 3. For each of the variables, use the print method for each variable. To print each varible
#print(int)
#print(float)
#print(string)
#print(boolean)
#print(boolean_other)
#print(list)
#print(dictionary)

# 4. Backtick ` in JS are used for Template literals. In a JS file a variable called intVariable and stringVariable exist.
# They are equal to the int and string variables on step 2.
# What is the python equvalent for: console.log(`int: ${intVariable}, string ${stringVariable}`)
#print(f'int: {int}, string: {string}')
# 5. Comment out all print statements up to this point
#done
# 6. Write a FOR LOOP in python that prints "David Rocks" 5 times
# Hint: type this into google "loop range python"
for _ in range(5):
    print("David Rocks")
# 7. Declare a function what print "Alex Rocks". Invoke that function 5 times. 
def print_alex_rocks():
    print("Alex Rocks")
for _ in range(5):
    print_alex_rocks()
# 8. Declare a function that takes in 2 parameters. 
# It will print "P1(your parameter1) and P2(your parameter2) Rocks"
# Now call that function using "Kyle" and "Winston" as the arguments 
# invoke that function 4 more times
def print_rocks(param1, param2):
    print(f"P1({param1}) and P2({param2}) Rocks")
print_rocks("Kyle", "Winston")
for _ in range(4):
    print_rocks("Kyle", "Winston")
# Definitions:  
# P is for Placeholder. P is for Parameters.
# These 2 start w/ the letter P 
# A parameter is variable in the declaration of the function - The place holder

# A is for actual value. A is for aguement.
# These 2 start w/ the letter A
# Arguement is are the values when calling the function - The actual value

# 9. Remember the list variable in step 2. 
# a. Print the index at 3. Then comment it out
#print(list[3])
# b. Now print the index at 100. Does this error? comment it out
#print(list[100])
# e. Now print the index at -1 index. Observe what it prints. Then comment it out
#print(list[-1])
# f. Now print the index at -100.  Does this error? comment it out
#print(list[-100])
# 10. Write a FOR LOOP in python that prints each item in the list variable in step 2.  
for item in list:
    print(item)
# The staring number MUST be a negative number. The ending number MUST be postive number
# Looking to get each item printed once in order and then a second time in order

# 11. Write a WHILE LOOP in python that does the same thing as 10. 
index = 0

while index < len(list):
    print(list[index])
    index += 1
# 12. For loops.
# Write a FOR LOOP in python that prints each item in list variable in step 2.  
# Hint: type this into google "loop python"

# 13. Repeat step 10 but instead of the list variable, use the dictionary variable. 
# Print each key
for key in dictionary:
    print(key)
# 14. Repeat step 13. Instead of printing each key, print each value
for key in dictionary:
    value = dictionary[key]
    print(value)
# Hint: google "dictionary values python"
