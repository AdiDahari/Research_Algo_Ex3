import doctest
import math


def last_call(f):
    '''
    This method is the decorator for using cache-like function calls.

    It holds within it a dict of function names,
    each entry of the outer dict holds within it another inner dict mapped by tuples of arguments.

    visually:
    dict _
          |- f1 (function name) -
          |                      |- tuple(1st_set_of_arguments) - f1(1st_set_of_arguments) (Result)
          |                      |- tuple(2nd_set_of_arguments) - f1(2nd_set_of_arguments)
          |- f2 -
                 |-tuple(...) - f2(...)
                 |-tuple(...) - f2(...)
        ...

    TESTS:

    >>> print(greet('Adi'))
    Hello Adi!
    >>> print(greet(name='Adi'))
    Cached Result: Hello Adi!
    >>> print(sum_str(1, 1))
    x + y = 2
    >>> print(sum_str(1, y=1))
    Cached Result: x + y = 2

    >>> print(sqrt_str(4))
    2.0
    >>> print(sqrt_str(4))
    Cached Result: 2.0

    '''
    call_dict = dict()

    def wrapper(*args, **kwargs):
        # matching nameless args to the parameters names
        varnames = f.__code__.co_varnames

        # assembling a dict of arguments of current call
        cached_args = dict()

        # adding all arguments both from args and kwargs
        for i in range(len(args)):
            cached_args.update({varnames[i]: args[i]})
        for key, val in kwargs.items():
            cached_args.update({key: val})

        # tupling the arguments for hashing
        tupled_args = tuple(cached_args.values())

        # checking if current call matches a cached one.
        # if first call of function - creating a new dict with it's name as a key.
        if tupled_args in call_dict.setdefault(f.__name__, dict()).keys():
            return f'Cached Result: {call_dict[f.__name__][tupled_args]}'

        # if no such call - add current result to cache and return it.
        else:
            call_dict[f.__name__][tupled_args] = f(
                *args, **kwargs)
            return call_dict[f.__name__][tupled_args]

    return wrapper


@last_call
def greet(name):
    return f'Hello {name}!'


@last_call
def sum_str(x, y):
    return f'x + y = {x + y}'


@last_call
def sqrt_str(x):
    return f'{math.sqrt(x)}'


if __name__ == '__main__':
    doctest.testmod()
