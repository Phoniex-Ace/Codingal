class InvalidRomanNumeralError(Exception):
    """Custom exception for invalid Roman numerals."""
    pass


class RomanConverter:
    def __init__(self):
        # Define mappings for Roman numeral conversions
        self.value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        self.roman_map = {symbol: value for value, symbol in self.value_map}

    def integer_to_roman(self, number):
        """Convert an integer to a Roman numeral."""
        if number == 0:
            raise ValueError("There is no Roman numeral for zero.")
        
        is_negative = number < 0
        remaining = abs(number)
        roman_numeral = ""

        for value, symbol in self.value_map:
            while remaining >= value:
                roman_numeral += symbol
                remaining -= value

        if is_negative:
            roman_numeral = "-" + roman_numeral

        return roman_numeral

    def roman_to_integer(self, roman):
        """Convert a Roman numeral to an integer."""
        if not isinstance(roman, str) or not roman:
            raise InvalidRomanNumeralError("Input must be a non-empty string.")
        
        roman = roman.upper()
        integer_value = 0
        i = 0
        
        while i < len(roman):
            # Check for two-character symbols first (e.g., "CM", "IX")
            if i + 1 < len(roman) and roman[i:i + 2] in self.roman_map:
                integer_value += self.roman_map[roman[i:i + 2]]
                i += 2
            elif roman[i] in self.roman_map:
                integer_value += self.roman_map[roman[i]]
                i += 1
            else:
                raise InvalidRomanNumeralError(f"Invalid Roman numeral symbol at position {i}: '{roman[i]}'")

        return integer_value

# Main Program
def main():
    converter = RomanConverter()

    print("Select an option:")
    print("1. Convert integer to Roman numeral")
    print("2. Convert Roman numeral to integer")

    choice = input("Enter 1 or 2: ")
    
    try:
        if choice == "1":
            # Integer to Roman numeral conversion
            number = int(input("Enter an integer to convert to Roman numeral: "))
            roman_numeral = converter.integer_to_roman(number)
            print("Roman numeral:", roman_numeral)

        elif choice == "2":
            # Roman numeral to integer conversion
            roman = input("Enter a Roman numeral to convert to an integer: ")
            integer_value = converter.roman_to_integer(roman)
            print("Integer value:", integer_value)

        else:
            print("Invalid choice. Please select 1 or 2.")
    
    except (TypeError, ValueError, InvalidRomanNumeralError) as e:
        print(f"Error: {e}")


# Run the main program
main()
