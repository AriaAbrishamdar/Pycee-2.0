import unittest

from pycee.errors import handle_name_error

class TestErrors(unittest.TestCase):

    def test_handle_name_error(self):
        result = handle_name_error("NameError: name 'arr' is not defined")
        expected_result = "https://api.stackexchange.com/2.2/search?site=stackoverflow&order=desc&sort=relevance&tagged=python&intitle=nameerror+name+is+not+defined"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()