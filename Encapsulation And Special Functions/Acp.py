class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string.strip()  # Remove leading/trailing whitespace

    def reverse_words(self):
        words = self.input_string.split()  # Split the string into a list of words
        reversed_words = [word[::-1] for word in words]  # Reverse each word
        reversed_string = ' '.join(reversed_words[::-1])  # Reverse the order of the words and join them back into a string
        return reversed_string

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    reverser = StringReverser(input_string)
    reversed_string = reverser.reverse_words()
    print("Reversed string:", reversed_string)