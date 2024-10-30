"""
Scope refers to accessibility
Variable scope : accessibility or visibility of variables in different parts of the program
 - Global Scope : variables declared outside any function or block code : are accessible anywhere in the program
 - Local Scope : variables declared withing functions i.e. accessed only inside the function
 - Block Scope : variables are declared withing a block of code
 - Function Scope : local scopes
 - Lexical/Enclosing/Non-local scope : a scope referenced in nested functions
 - Built in scope : variables available inside of built in functions
"""

global_var = "I am string global"

def example():
    local_Var = "I am local variable"
    print(global_var)
    print(local_Var)

example() # inside function
print(global_var) # outside function

# enclosing  :: nested functions
def outer_function():
    # the variables defined in the outer function are accessible within the inner functions
    outer_Var = "this is the outer variable"
    def inner_function():
        # variables in the inner function are only accessible to the inner function
        inner_var = "this it the inner function variable"
        print(outer_Var)
        print(inner_var)

    inner_function()
    # print(inner_var)


# built in scope :: accesssed anywhere in code



