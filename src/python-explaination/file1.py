f = 10.5
i = 10
s = "string"
a = [1, "two", 3.0, [1, 2, 3]]
d = {"key1": "value1", "key2": 2, "key3": [1, 2, 3]}
b = False

def hello(t):
    print("From Hello, {}".format(t))

hello("Hello")

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello from {}".format(self.name))

m = MyClass("MyClass Instance")
m.greet()

print("Hello, World!")