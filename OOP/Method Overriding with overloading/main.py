# Scenario: Override the parent class method, but with boolean type param, overload the child class method & call the parent class method

class A:
    def sum(self):
        print("Calling from A")

class B(A):
    def sum(self, call_super=False):
        if call_super:
            super().sum()
        else:
            print("Calling from B")

obj1=B()
obj1.sum(call_super=True)
