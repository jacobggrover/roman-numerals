# Started around 2:45 pm 21 Aug 2020
# Finished at 6:22 pm 21 Aug 2020

# Global list for converting integers to roman numerals. I didn't know how to make the dictionary work.
NUMERALS = [
    ['I', 1],
    ['V', 5],
    ['X', 10],
    ['L', 50],
    ['C', 100],
    ['D', 500],
    ['M', 1000]
    ]

# For converting roman numerals to integers, a dictionary was much more useful
VALUES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}

# This is only used for a help prompt, I put it up here so if you wanted to change the numerals you can do it all in one place.
VALID_NUMERALS = "I, V, X, L, C, D, and M"
        
# Used in checking the subtractive notation
def is_power_of_ten(input_number):
    i = 1
    while i <= input_number:
        if i == input_number:
            return True
        i = i * 10
    return False

def int_to_roman_string(input_number):
    if isinstance(input_number, int) == False or input_number <= 0:
        print("Error: Input is not a positive integer")
        return ""
    
    roman_string = ""
    x = input_number
    i = len(NUMERALS) - 1
    
    while x >= 0 and i >= 0:
        # If the remainder is bigger than the current digit, add it.
        if x >= NUMERALS[i][1]:
            while x >= NUMERALS[i][1]:
                x -= NUMERALS[i][1]
                roman_string += NUMERALS[i][0]
                
        #Check for the possibility of subtractive notation for the next digits.
        string_altered = False
        
        if i > 0:
            j = 0
            while j < i and not string_altered:
                if NUMERALS[i][1] != 2 * NUMERALS[j][1]\
                   and x - (NUMERALS[i][1] - NUMERALS[j][1]) >= 0\
                   and NUMERALS[i][1] / NUMERALS[j][1] <= 10\
                   and is_power_of_ten(NUMERALS[j][1]):#This line elimanates a problem with 45 being written as VL instead of XLV
                    string_altered = True
                    x -= (NUMERALS[i][1] - NUMERALS[j][1])
                    roman_string = roman_string + NUMERALS[j][0] + NUMERALS[i][0]
                j += 1
        i -= 1
        
    if x < 0 or i < -1:
        print("Error: \"NUMERALS\" wasn't defined suitably.")
        
    return roman_string

def is_valid(roman_string):
    if not isinstance(roman_string, str):
        return False
    
    for i in range(1, len(roman_string)):
        if roman_string[i] not in VALUES.keys():
            return False
        
    return True

def roman_string_to_int(raw_string):
    roman_string = raw_string.upper()
    if not is_valid(roman_string):
        print("Error: Input is not a valid Roman Numeral. Valid digits are " + VALID_NUMERALS)
        return 0
    
    output_number = 0
    i = 0
    
    while i < len(roman_string):
        computed_as_subtractive = False
        if i < len(roman_string) - 1:
            diff = VALUES[roman_string[i+1]] - VALUES[roman_string[i]]
            if diff > 0:
                computed_as_subtractive = True
                i += 2
                output_number += diff
                
        if not computed_as_subtractive:
            output_number += VALUES[roman_string[i]]
            i += 1
    return output_number

def help():
    print("Enter 'R' to convert Roman Numerals to regular numbers")
    print("Enter 'I' to convert regular numbers to Roman Numerals")
    print("Enter '?' to see this message again")
    print("Enter 'Q' to quit")
    return

def main():
    # The next few lines can be uncommented to check the functionality of the code
    #for i in range(1, 101):
        #s = int_to_roman_string(i)
        #print(s, roman_string_to_int(s))

    # Otherwise, I made a nice little menu for you. :)
    print("Welcome to the Roman Numeral Converter!")
    help()
    
    running = True
    mode = "main_menu"
    
    while running:
        if mode == "main_menu":
            action = str(input("==> :"))
            action = action.upper()
            if action == '?':
                help()
            elif action == 'Q':
                print("Goodbye!")
                running = False
            elif action == 'I':
                mode = "int_to_roman"
                print("Enter 'Q' to return to the main menu")
            elif action == 'R':
                mode = "roman_to_int"
                print("Enter 'Q' to return to the main menu")
                
        elif mode == "roman_to_int":
            r = str(input("Enter a Roman Numeral: "))
            if r.upper() == 'Q':
                mode = 'main_menu'
            else:
                x = roman_string_to_int(r)
                if x != 0:
                    print (r.upper() + " = " + str(x))
                
        elif mode == 'int_to_roman':
            x = str(input("Enter number to be converted: "))
            if x.upper() == 'Q':
                mode = "main_menu"
            else:
                r = int_to_roman_string(int(x))
                if r == "":
                    print("Please enter a positive integer, negative numbers and decimals are not supported.")
                else:
                    print("Roman Numeral of " + str(x) + ":  " + r)
                
if __name__ == "__main__":
    main()










            
        
