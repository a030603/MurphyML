import numpy as np


def test_array_sum():
    array1 = np.array([1, 2, 3])
    array2 = np.array([1, 2, 3])
    array3 = np.array([2, 4, 6])

    assert np.array_equal(array1 + array2, array3)


def test_array_argmax():
    x = np.array([3, 2, 4, 1])

    actual = x.argmax(axis=0)

    assert actual == 2


def test_array_argmax2():
    array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

    actual = array.argmax(axis=0)

    assert actual.ndim == 2
    assert np.array_equal(actual.shape, np.array([2, 2]))
    assert np.array_equal(actual, np.array([[2, 2], [2, 2]]))


def test_repeat():
    matrix_1dm = np.random.randn(1, 4)
    matrix_2dm = matrix_1dm.repeat(5, axis=0)

    assert matrix_2dm.shape == (5, 4)


def test_sum():
    matrix_2dm = np.random.randn(4, 7)
    matrix_1dm = matrix_2dm.sum(axis=1, keepdims=True)

    assert matrix_1dm.shape == (4, 1)


def test_matmul():
    x = np.array([[1, 2], [3, 4]])

    assert np.array_equal(np.matmul(x, x), np.array([[7, 10], [15, 22]]))


def test_deepcopy():
    x = np.random.randn(4, 5)
    y = np.zeros_like(x)
    y2 = x.copy()

    y[...] = x
    y, y2 = y + 1, y2 + 1

    assert not np.array_equal(x, y)
    assert not np.array_equal(x, y2)


def test_shallow_copy():
    x = np.random.rand(4, 5)
    y = x.view()

    y += 1  # y + 1 returns new array, y += 1 modifies array

    assert np.array_equal(x, y)


def test_array_indexing():
    x = np.array([[1, 2], [3, 4]])
    rows = np.array([0, 1])
    cols = np.array([0, 1])

    actual = x[rows, cols]
    expected = np.array([1, 4])

    assert np.array_equal(actual, expected)


def test_array_indexing2():
    x = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8],
                  [9, 10, 11]])
    rows = np.array([[0, 0],
                     [3, 3]])
    cols = np.array([[0, 2],
                     [0, 2]])

    actual = x[rows, cols]
    expected = np.array([[0, 2],
                         [9, 11]])

    assert np.array_equal(actual, expected)


def test_transpose_2x2():
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[1, 3], [2, 4]])

    assert np.array_equal(x.transpose(), y)


def test_transpose_2x2x2():
    x = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    y = np.array([[[1, 3], [5, 7]], [[2, 4], [6, 8]]])

    assert np.array_equal(x.transpose((2, 0, 1)), y)


def test_predicate():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = x % 2 == 0

    assert np.array_equal(y, [False, True, False, True, False, True, False, True])


def test_filter_by_predicate():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = x[x % 2 == 0]

    assert np.array_equal(y, [2, 4, 6, 8])
