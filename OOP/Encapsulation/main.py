class MyClass:
    def __init__(self):
        self.public_variable = "Public"
        self._protected_variable = "Protected"
        self.__private_variable = "Private"

    def get_private_variable(self):
        return self.__private_variable
    
    def set_private_variable(self, val):
        self.__private_variable = val


obj = MyClass()

obj.set_private_variable("Private (Updated)") # Require to use setter rather than trying to change the value of a private variable

print(obj.public_variable)  # Output: Public
print(obj._protected_variable)  # Output: Protected
# This will raise an AttributeError because __private_variable is considered private
# print(obj.__private_variable)

# Accessing private variable using a method
print(obj.get_private_variable())  # Output: Private
