import sys

print("Classic hello world!")
x = input("Enter the name of the city you were born in: ")  # Inputs are always strings
y = input("Enter the name of your first pet: ")  # Here x, y and z are all strings.
z = x + y  # To convert it to a different data type add the data type within the input scope.

print("String concatination")
print(x + " " + y)

#######################################################################################################################

print("Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("How to create a new line? - \n")

print("Hello " + input("Hi! What is your name? ") + "!")

#######################################################################################################################

print("You can calculate length of the string using len()")
temp = input("Enter the string to calculate the length")
len(temp)

print("To get the size of the string in bytes you can use sys.getsizeof()")
# Need to import sys

print("import sys")
temp = input("Enter the string to calculate the size in bytes")
sys.getsizeof(temp)
# Don't call your string variable str. It shadows the built-in str() function.

#######################################################################################################################

x = input("What is your name? \n")
y = len(x)

# Demonstration of F strings

print(f"The length of the string you entered is: {y}")

w = sys.getsizeof(x)
print(f"The size of string in bytes is: {w}")

print(len(input("What is your name?")))

#######################################################################################################################

print("String Concatinator")
city = input("What is the name of the city you grew up in?\n")
pet = input("What is the name of your first pet?\n")
print("Concatination of the strings is " + city + " " + pet)