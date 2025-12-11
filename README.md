# python-input-validation

## Overview
This is a simple Python script that asks the user to enter a number, validates the input, converts it to the correct number type (integer or float), and calculates the square root.  
It’s designed to practice Python basics such as:

- Loops (`while`)
- Exception handling (`try/except`)
- Type conversion (`float` and `int`)
- Using the `math` library

## How to Use
1. Run the script using Python3.  
2. The program will ask you to enter a number.  
3. If the input is invalid (not a number), it will keep asking.  
4. Once a valid number is entered, the script prints its square root.

## Input Handling
This script safely manages user input to prevent errors during number conversion. Since `input()` always returns a string, the program:

- Uses a loop to repeatedly ask for valid input  
- Converts input into a number using `float()`  
- Catches invalid input with `try/except`  
- Identifies whole numbers so the output is printed cleanly (e.g., `5` instead of `5.0`)

## Key Learning Points
- Handling user input safely  
- Understanding that `input()` always returns a string  
- Converting strings to numbers for calculations  
- Checking for whole numbers to print clean output  
