# Decorator Functions
def check_pin(method):
    # Access all the methods & attributed using the "ref" param; 
    # *args & **kwargs will be passed if the method has extra params other than self which is will get decorated using this function.
    def wrapper_func(ref):
        if ref.pin != '':
            # print(ref.pin)
            # print(ref.balance)
            user_pin = input("Enter pin: ")
            if ref.pin == user_pin:
                return method(ref)  # returns to the method which is being decorated.
            else:
                print("Invalid pin!")
                return ref.menu()
        else:
            return ref.create_pin()
    return wrapper_func


def halt_create_pin(method):
    def wrapper_func(ref):
        if ref.pin != '':
            print("""
                Pin is already created!
                Did you mean reset pin? Then, please select "Option 5" from the menu.
            """)
            ref.menu()
        else:
            return method(ref)
    return wrapper_func
