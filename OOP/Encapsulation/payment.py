class Payment:
    def __init__(self, price) -> None:
        self.__final_price = price + price * 0.05   # Private Var
    
    def get_final_price(self):
        return self.__final_price
    
    def set_final_price(self, discount):
        self.__final_price = self.__final_price - self.__calculate_final_price(discount)

    # Priavte method
    def __calculate_final_price(self, discount):
        return self.__final_price * discount
    
book = Payment(10)
discount = 0.15
if discount > 0:
    book.set_final_price(discount)
print(book.get_final_price())