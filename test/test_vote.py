import unittest
import sys

sys.path.append('../vote')
from updownvote import *

class TestVote(unittest.TestCase):

    def test_updowndata(self):
        result = updowndata(solution_link='https://stackoverflow.com/questions/14804084/python-nameerror-name-is-not-defined/14804107#14804107',
                            error_type='NameError',
                            value=1)

        expected_result = {"solution_link": "https://stackoverflow.com/questions/14804084/python-nameerror-name-is-not-defined/14804107#14804107",
                                  "error_type": "NameError",
                                  "value": 1}

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()