import unittest

import numpy as np


class NumpyTest(unittest.TestCase):

    def test_array_um(self):
        array1 = np.array([1, 2, 3])
        array2 = np.array([1, 2, 3])
        array3 = np.array([2, 4, 6])

        self.assertTrue(np.array_equal(array1 + array2, array3), "array sum must equal")


if __name__ == '__main__':
    unittest.main()
