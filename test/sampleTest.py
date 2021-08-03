import unittest


class SampleTest(unittest.TestCase):

    def test_sample(self):
        self.assertTrue(True, "always pass")

    def test_str(self):
        subStr = 'hihi'
        fullStr = f"\u0394\u2341{subStr}"

        self.assertEqual(type(fullStr), str)


if __name__ == '__main__':
    unittest.main()
