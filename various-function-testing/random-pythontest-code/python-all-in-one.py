##############################
# Purpose: Play with python in all in one program for interview practice.
# Usefulness : This program is very useful for quick reference during your interview round and can work as cheat sheet
#
##############################
#Convert a string into a python list
def string_to_list(string):
    placeholder_as_list = list(string.split(" "))
    print("Value in placeholder_as_list is:{}".format(placeholder_as_list))
    for i in placeholder_as_list:
        print("-->{}".format(i), end="\t")

def replace_word_in_string(string,word_to_replace,replace_with):
    replaced_string = string.replace(word_to_replace,replace_with,1)
    print("Replaced string is '{}'".format(replaced_string))

def suffix_character(string,suffix):
    #NOTE: String is unmutable data type so please first convert into mutable.
    # NOTE: Make sure you choose correct data structure in python as only list and dictionaries are mutable DS.
    new_string = list(string.split(" "))
    new_string.append(suffix)
    print("String with Suffix:{}".format(' '.join(new_string)))

def print_star_triangle():
    tree_length=10
    for i in range(tree_length):
        for j in range(tree_length - i):
            print(" ",end="")
        for k in range(1,i):
            l=0
            while l <= 1:
                print("*",end="")
                l+=1
        print("",end="\n")

def add_multi_dimension_array():
    a = [[1,2,3],[4,5,6],[7,8,9]]
    b = [[1,2,3],[4,5,6],[7,8,9]]
    c = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            c[i][j] = a[i][j] + b[i][j]

    for result in c:
        print(result)

# Common area
placeholder = 'shailender is good in algorithm designing'

# Task 1: Convert string into list.
#string_to_list(placeholder)

# Task 2: Replace word with another word in a string.
#replace_word_in_string(placeholder,'good','bad')

# Task 3: Suffix string with a character.
#suffix_character(placeholder, ".")

# Task 4: Print * triangle
#print_star_triangle()

# Task 5: Add multi dimensional values
add_multi_dimension_array()