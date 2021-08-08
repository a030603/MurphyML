import unittest


# unittest sample
class SampleTest(unittest.TestCase):

    def test_sample(self):
        self.assertTrue(True, "always pass")

    def test_str(self):
        subStr = 'hihi'
        fullStr = f"\u0394\u2341{subStr}"

        self.assertEqual(type(fullStr), str)


# pytest sample
def test_sample2():
    assert 1 < 2


if __name__ == '__main__':
    unittest.main()
