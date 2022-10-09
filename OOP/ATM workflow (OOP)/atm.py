# Ref: https://www.youtube.com/watch?v=Mf2RdpEiXjU

from decorators import check_pin, halt_create_pin

class Atm:
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.menu()
    
    @property
    def pin(self):
        return self.__pin
    
    @pin.setter
    def pin(self):
        self.reset_pin()

    def menu(self):
        user_input = int(input("""
            Hello, how do you like to proceed?
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Reset pin
            6. Exit
        """))

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        elif user_input == 5:
            self.reset_pin()
        elif user_input == 6:
            print("Exiting from the application!")
            exit()
        else:
            print("Invalid input! Choose between option 1-5")
            return self.menu()
    
    @halt_create_pin
    def create_pin(self):
        user_input = input("Create pin: ")
        self.__pin = user_input
        print("Pin set succesfully!")
        return self.menu()

    @check_pin
    def deposit(self):
        deposit_value = float(input("How much you want to deposit? "))
        self.__balance = deposit_value
        print(f"{self.__balance} is credited to your account!")
        return self.menu()
    
    @check_pin
    def withdraw(self):
        withdraw_value = float(input("How much you want to withdraw? "))
        if self.__balance > withdraw_value:
            self.__balance = self.__balance - withdraw_value
            print(f"""
                {withdraw_value} is withdrawn from your account!
                Current Balance: {self.__balance}
            """)
            self.menu()
        else:
            print("Insufficient balance!")
            self.menu()
    
    @check_pin
    def check_balance(self):
        print(f"Your balance is: {self.__balance}")
        self.menu()
    
    @check_pin
    def reset_pin(self):
        new_pin = input("Enter new pin: ")
        if self.__pin == new_pin:
            print("Cannot create a new pin similar to your previous pin!")
            return self.reset_pin()
        else:
            self.__pin = new_pin
            print("New pin is successfully set!")
            return self.menu()
