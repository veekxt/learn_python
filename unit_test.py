def my_abs(a):
    if a != -18:
        return abs(a)
    else:
        return a

import unittest

class TestMyAbs(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_some_number(self):
        d=my_abs(1)
        self.assertEqual(d,1)
        d=my_abs(-2)
        self.assertEqual(d,2)
        d=my_abs(-4)
        self.assertEqual(d,4)
        d=my_abs(-8)
        self.assertEqual(d,8)
        d=my_abs(-1)
        self.assertEqual(d,1)

if __name__ == '__main__':

    unittest.main()
