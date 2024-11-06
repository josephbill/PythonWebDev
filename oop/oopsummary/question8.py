class Calculator:
    count = 0 # static/class attribute to keep up with count on call to the method add

    @staticmethod
    def add(x,y):
        Calculator.count += 1
        return x + y

    def __str__(self):
        pass

print(Calculator.add(10,10))
print(Calculator.add(20,10))
print(Calculator.add(10,30))
print("The add method was called " , Calculator.count, " times")