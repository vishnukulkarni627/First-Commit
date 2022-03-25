# Decorator
# 1. Outer function should accept only one argument
# 2. Outer function argument will be having address of main function
# 3. Variable name should be different
# 4. wrapper class will return main function address
#  Demo program
def spam(func):
    def wrapper(*args, **kwargs):
        print("execute first later main function")
        return func(*args, **kwargs)
    return wrapper


@spam
def add(a, b):
    return a + b



print(add(1, 2))


# log a message

