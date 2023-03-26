from time import time


def timer(f, *args, **kwargs):
    """
    Measure the execution time of a function and return the result in seconds.

    Parameters:
    f (function): The function to be measured.
    *args: Variable length argument list to be passed to the function.
    **kwargs: Arbitrary keyword arguments to be passed to the function, for example name = yehuda heller.

    Returns:
    float: The time in seconds that it took to execute the function.

    """
    start_count = time()
    f(*args, **kwargs)
    end_count = time()
    execution_time = end_count - start_count
    return execution_time


# Example usage
res1 = timer(print, "Hello")
res2 = timer(zip, [1, 2, 3], [4, 5, 6])
res3 = timer("Hi {name}".format, name="Bug")

print(res1, res2, res3)
