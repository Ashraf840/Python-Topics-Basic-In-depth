# Scenario: 2 separate classes contain same method. Based on class object, the method invocation will be different.

class French:
    def say_hello(self):
        print("Bonjour")

class Chinese:
    def say_hello(self):
        print("你好")

def intro(obj):
    obj.say_hello()

john=French()
yin=Chinese()

intro(john)
intro(yin)