import time
from functools import wraps


def timer(func):
    """
    A decorator that prints how long a function took to run.
    :param func: function being decorated.
    :return: callable, the decorated function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # When wrapper() is called, get the current time:
        start_time = time.time()
        # Call the decorated function and store the result
        function_result = func(*args, **kwargs)
        # Get the total time it took to run and print it out.
        total_time = time.time() - start_time
        print(f'{func.__name__} took {total_time}s to run.')
        return function_result

    return wrapper


def print_return_type(func):
    """
    A decorator that prints out the type of the variable that gets returned from every call of any function it is
    decorating (from DataCamp)

    :param func: the function being decorated

    :return: callable: the decorated function. When called, something will be printed to stdout.
    """

    # Define wrapper(), the decorated function
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Call the function being decorated
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned type type(result)')
        return result

    # Return the decorated function
    return wrapper


def counter(func):
    """
    Decorator to count the number of times a callable is called.
    :param func: the function being decorated
    :return: callable: the decorated function. Access the count using 'func.count'.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func

    # Set count to 0 to initialize call count for each new decorated function
    wrapper.count = 0
    # Return the new decorated function
    return wrapper
