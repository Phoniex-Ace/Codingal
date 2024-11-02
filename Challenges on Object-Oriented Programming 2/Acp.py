class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def convert_to_roman(self):
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman_numeral = ""
        remaining = self.number

        for (value, symbol) in value_map:
            while remaining >= value:
                roman_numeral += symbol
                remaining -= value

        return roman_numeral

# Getting user input
try:
    number = int(input("Enter an integer to convert to Roman numeral: "))
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        converter = IntegerToRoman(number)
        print("Roman numeral:", converter.convert_to_roman())
except ValueError:
    print("Invalid input. Please enter a valid integer.")
