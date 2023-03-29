from functools import wraps


def type_check(correct_type):

    def type_check_decorator(func):
        @wraps(func)
        def wrapper(arg):
            if not isinstance(arg, correct_type):
                raise InvalidTypeError(f"Error! Expected to got {correct_type}.")
            return func(arg)
        return wrapper
    return type_check_decorator


class InvalidTypeError(Exception):
    pass


@type_check(int)
def times2(num):
    return num*2

@type_check(list)
def times_list(The_list):
    new_list = []
    for item in The_list:
        new_list.append(item*2)
    return new_list


if __name__ == "__main__":
    try:
        # correct examples
        print(times2(5))
        print(times_list([2, 2, 2]))

        # incorrect examples
        print(times2([5, 5]))
        print(times_list("hello"))

    except InvalidTypeError as error:
        print(error)