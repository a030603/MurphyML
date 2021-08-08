import unittest

import numpy as np


class NumpyTest(unittest.TestCase):

    def test_array_sum(self):
        array1 = np.array([1, 2, 3])
        array2 = np.array([1, 2, 3])
        array3 = np.array([2, 4, 6])

        self.assertTrue(np.array_equal(array1 + array2, array3), "array sum must equal")

    def test_array_argmax(self):
        array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

        actual = array.argmax(axis=0)

        self.assertEqual(actual.ndim, 2)
        self.assertTrue(np.array_equal(actual.shape, np.array([2, 2])))
        self.assertTrue(np.array_equal(actual, np.array([[2, 2], [2, 2]])))


if __name__ == '__main__':
    unittest.main()
