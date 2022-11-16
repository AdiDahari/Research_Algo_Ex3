import doctest


class List(list):
    '''
    This class is an extention for built-in list type.


    TESTS:

    >>> mylist = List([[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]]])

    >>> print(mylist)
    [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]]]

    >>> print(mylist[0, 1, 3])
    66

    >>> print(mylist[0])
    [[1, 2, 3, 33], [4, 5, 6, 66]]

    >>> print(mylist[0, 0, 0])
    1

    >>> print(mylist[-1, -1, -1])
    188

    >>> print(mylist[0, 0, 4])
    Traceback (most recent call last):
        ...
    IndexError: list index out of range

    >>> print(mylist[0, 2, 0])
    Traceback (most recent call last):
        ...
    IndexError: list index out of range

    >>> print(mylist[3, 0, 0])
    Traceback (most recent call last):
        ...
    IndexError: list index out of range

    '''

    def init(self, *args):
        super(List, self).__init__(*args)

    def __getitem__(self, indices):
        '''
        This overloaded operator is the squared brackets operation [...]
        by overloading this operator it is possible to access deep list (multiple layers) values
        by appending the indices within a single squared brackets pair. 
        '''
        if isinstance(indices, tuple):  # if multiple indices
            first = indices[0]  # splitting to first and rest
            indices = indices[1:]
            desired = super(List, self).__getitem__(
                first)  # using super's getitem
            for i in indices:
                desired = desired[i]  # going deep in layers
            return desired

        # single-layered list - return super's getitem result
        return super(List, self).__getitem__(indices)

    def __setitem__(self, indices, value):
        '''
        This overloaded operator is the setter for setting a specific value within the list to desired value.
        Similarly to getitem, it goes deep within the list's layers,
        stops at the second-last layer - and changes the desired index of it to the value.
        '''
        if isinstance(indices, tuple):  # multi-layer
            first = indices[0]
            last = indices[-1]  # keeping the last index
            desired = super(List, self).__getitem__(first)
            for i in range(len(indices) - 2):  # going deep to second-last layer
                desired = desired[indices[i]]
            desired[last] = value  # setting the value of the desired index
        else:
            super(List, self).__setitem__(indices, value)  # single-layer


if __name__ == '__main__':
    doctest.testmod()
