def functionName():
    return "This is the return from function"

#functionName()

# a function with parameters (a,b)
def function_with_params(a,b):
    print(a)

# callbacks : functions passed to other functions as arguments
function_with_params(functionName(),2)  # 2,2 are called arguments


def outer_function(text):
    def inner_function():
        return text
    return inner_function()

closure_func = outer_function("Hello class ,from Closure")
print(closure_func)
