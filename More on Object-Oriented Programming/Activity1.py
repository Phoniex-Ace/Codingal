class IOString():
    def __init__(self):
        self.str1 = ""
    def Get_String(self):
        self.str1 = input("Enter String: ")
    def print_string(self):
        print("The Result Is: ",self.str1.upper())

str1 = IOString()

str1.Get_String()
str1.print_string()