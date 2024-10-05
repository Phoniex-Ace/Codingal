class Employee:
    def __init__(self):
        print('Employee Created')
    def __del__(self):
        print("Destructor Called")

def Create_Obj():
    print('Making Object')
    obj = Employee()
    print('Function end...')
    return obj

print('Calling Create_obj() function.....')
obj = Create_Obj()
print('Program End....')