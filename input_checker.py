import math

# This variable helps us repeat the question until the user enters a valid number
isNumber = False

while not isNumber:
    # Ask the user to enter a number
    # IMPORTANT: inpot() ALWAYS returns a string, even if the user types a numbnber
    number = input("Enter a number: ")
    try:
        # Try converting the strign to a float
        number = float(number)
        isNumber = True # Conversion successful -> exit loop
    except ValueError:
        # If conversion fails, the user didn't type a valid number
        print("Invalid input. Please enter a valid number.")

# If the number is a whole number (like 25.0), convert it to int for clean printing
if number.is_integer():
    number = int(number)
# When we have a valid number, calculate its square root
print(f"square root of {number} is {math.sqrt(number)}")



