

# 1. Write a program that sum of all elements:
one = [613, 955, 291, 497, 562, 483, 165, 210, 864, 789]
sum = 0
for element in one:
    sum += element
print("The sum of all elements is:", sum)
# 2.  Write a program that find the largest element:
two = [386, 850, 274, 316, 526, 937, 998, 249, 269, 922]

largest_element = two[0]

for element in two:
    if element > largest_element:
        largest_element = element

print("The largest element is:", largest_element)

# 3. Write a program that duplicates that doubles the value of each elements in the list:
# for example: [1,2,3] should result in [2,4,6]
three = [211, 36, 295, 455, 147, 977, 381, 253, 327, 617]

doubled_list = []

for element in three:
    doubled_value = element * 2
    doubled_list.append(doubled_value)

print("Original list:", three)
print("Doubled list:", doubled_list)
# 4. Write a program that concatenates these two list into a single list:
four_a = [582, 427, 534, 143, 567, 604, 12, 48, 686, 825]
four_b = [357, 728, 406, 989, 380, 800, 201, 410, 452, 141]

new_list = four_a + four_b

print("Concatenated List:", new_list)

# 5. Write a program that removes a specific element from a list by its value.
five = [456, 942, 944, 762, 836, 451, 314, 559, 954, 211]

element_to_remove = 451

if element_to_remove in five:
    five.remove(element_to_remove)
    print(f"Element {element_to_remove} removed.")
else:
    print(f"Element {element_to_remove} not found in the list.")

print("Updated List:", five)
# 6. Write a program that removes a specific element from a list by its index.
six = [993, 245, 896, 250, 226, 313, 918, 877, 793, 695]

index_to_remove = 4 

if 0 <= index_to_remove < len(six):
    removed_element = six.pop(index_to_remove)
    print(f"Element {removed_element} removed.")
else:
    print("Invalid index.")

print("Updated List:", six)


# 7. Write a program that sorts a list of numbers in ascending order.
seven = [887, 106, 368, 603, 35, 455, 728, 449, 108, 47]

sorted_list = sorted(seven)

print(sorted_list)

# 8. Write a program that filters out all elements in a list that are less than a specified value.
# use for loop and conditionals
eight = [309, 122, 27, 240, 453, 174, 193, 649, 804, 171]
threshold = 200

filtered_list = []

for element in eight:
    if element >= threshold:
        filtered_list.append(element)

print("Filtered List (elements >= 200):", filtered_list)

# 9. Calculate and print the length (number of elements) of a given list.
nine = [679, 697, 657, 171, 503, 582, 656, 82, 724, 796]

length_of_list = len(nine)

print("Length of the list:", length_of_list)

# 10. Write a program that take a list and print a subset of its elements by specifying a start and end index.
ten = [64, 800, 662, 185, 630, 612, 181, 210, 738, 12]
start_index = 1
end_index = 4


subset = ten[start_index:end_index + 1]

print("Subset of elements:", subset)

# 11. Write a program iterates the list and
# prints 'FizzBuzz' when divisable by 3 and 5.  
# prints 'Fizz' when divisable by 3 .  
# prints 'Buzz' when divisable by 5. 
eleven = [213, 927, 265, 39, 860, 421, 550, 884, 991, 1500]

for number in eleven:
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

# 12. Write a program that appends an element to the end of a list.
twelve = [36, 632, 155, 350, 746, 642, 113, 534, 9, 34]

element_to_append = 999 

twelve.append(element_to_append)

print("Updated List:", twelve)
# 13. Write a program that inserts an element at a specific position in a list.
thirteen = [191, 871, 990, 163, 687, 747, 606, 799, 373, 851]
element_to_insert = 4


position_to_insert = 5

thirteen.insert(position_to_insert, element_to_insert)

print("Updated List:", thirteen)
# 14. Write a program that counts how many times a specific element appears in a list.
fourteen = [1, 1, 1, 2, 2, 1, 3, 3, 2, 1]
element_to_count = 1

count_of_element = fourteen.count(element_to_count)

print(f"The element {element_to_count} appears {count_of_element} times in the list.")

# try using for loop and conditional
# and then try .count() method


# 15.  Write a program that extracts all even numbers from a list and stores them in even_only:
# use for loop and conditionals
fifteen = [267, 688, 88, 755, 680, 746, 559, 710, 283, 451]
even_only = []

for number in fifteen:
    if number % 2 == 0:
        even_only.append(number)

print("Even Numbers Only:", even_only)


# 16. Write a program that reverses this list but does not change the original sixteen variable:
# The answer is not sixteen.reverse(). 
sixteen = [378, 763, 856, 566, 847, 795, 313, 540, 67, 219]

reversed_sixteen = sixteen[::-1]

print("Reversed List (original unchanged):", reversed_sixteen)

# 17. Write a flattens this double nested listbelow:
# Result should be [1, 2, 3, 4, 5, 6, 7, 8]
# Hint: try a nested loop (2 for in loops) 
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

flattened_list = []

for inner_list in nested_list:
    for item in inner_list:
        flattened_list.append(item)

print("Flattened List:", flattened_list)
# 18. Write a program that finds duplicates from the 2 lists below:
# Hint: try a nested loop (2 for in loops) and use equality
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

duplicates = []

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            duplicates.append(item1)

print("Duplicates:", duplicates)
