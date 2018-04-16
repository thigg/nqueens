import unittest
from hundredsemesterslater import *


class MyTest(unittest.TestCase):
    """
    Test the n-queens python implementation
    """

    def testInvalidParams(self):
        """
        tests invalid parameters.
        """
        with self.assertRaises(ValueError):
            nqueens(-1)
            nqueens(0)
            nqueens(1.5)
            nqueens("1")

    def testSmallN(self):
        """
        tests small arguments for quick tests.
        """
        # Solutions from wikipedia!
        for idx, solution in enumerate([1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680]):
            self.assertEqual(nqueens(idx + 1), solution)

            # def test12(self):
        self.assertEqual(nqueens(12), 14200)

    #def test13(self):
    #    self.assertEqual(nqueens(13), 73712)
