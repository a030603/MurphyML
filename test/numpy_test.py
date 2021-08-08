import unittest

import numpy as np


def test_array_sum():
    array1 = np.array([1, 2, 3])
    array2 = np.array([1, 2, 3])
    array3 = np.array([2, 4, 6])

    assert np.array_equal(array1 + array2, array3)


def test_array_argmax():
    array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

    actual = array.argmax(axis=0)

    assert actual.ndim == 2
    assert np.array_equal(actual.shape, np.array([2, 2]))
    assert np.array_equal(actual, np.array([[2, 2], [2, 2]]))


if __name__ == '__main__':
    unittest.main()
