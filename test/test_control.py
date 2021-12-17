import unittest

from pycee.control import (
    get_error_detail,
    get_error_info_from_traceback,
    get_error_message,
    get_error_type,
    get_error_line,
    get_code,
    get_offending_line,
)

traceback = """Traceback (most recent call last):
  File "example_code.py", line 1, in <module>
    print(arr[0])
NameError: name 'arr' is not defined"""
code = """print(arr[0])"""
error_info = {'success_message': 'Success',
              'traceback': 'Traceback (most recent call last):\n  File "example_code.py", line 1, in <module>\n    print(arr[0])\nNameError: name \'arr\' is not defined',
              'message': "NameError: name 'arr' is not defined",
              'type': 'NameError',
              'line': 1,
              'file': 'example_code.py',
              'code': 'print(arr[0])',
              'offending_line': 'print(arr[0])'}
path = "test_code.py"

class TestControl(unittest.TestCase):

    def test_get_error_detail(self):
        result = get_error_detail(traceback=traceback,
                                  _code=code)

        expected_result = error_info

        self.assertEqual(result, expected_result)


    def test_get_error_info_from_traceback(self):
        result = get_error_info_from_traceback(traceback, code)
        expected_result = error_info

        self.assertEqual(result, expected_result)


    def test_get_error_message(self):
        result = get_error_message(traceback)
        expected_result = "NameError: name 'arr' is not defined"

        self.assertEqual(result, expected_result)


    def test_get_error_type(self):
        result = get_error_type("NameError: name 'arr' is not defined")
        expected_result = "NameError"

        self.assertEqual(result, expected_result)


    def test_get_error_line(self):
        result = get_error_line("NameError: name 'arr' is not defined")
        expected_result = None

        self.assertEqual(result, expected_result)


    def test_get_code(self):
        result = get_code(path)
        expected_result = """def some_function()
    msg = 'hello, world!'
    print(msg)
     return msg"""

        self.assertEqual(result, expected_result)


    def test_get_offending_line(self):
        result = get_offending_line(1, code)
        expected_result = "print(arr[0])"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()