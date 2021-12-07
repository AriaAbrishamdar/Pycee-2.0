import unittest

from pycee.answers import _ask_stackoverflow, _ask_google, _get_answer_content, sort_by_updownvote, getSummary
from pycee.utils import Answer, Question

error_info = {'success_message': 'Success',
              'traceback': 'Traceback (most recent call last):\n  File "example_code.py", line 1, in <module>\n    print(arr[0])\nNameError: name \'arr\' is not defined',
              'message': "NameError: name 'arr' is not defined",
              'type': 'NameError',
              'line': 1,
              'file': 'example_code.py',
              'code': 'print(arr[0])',
              'offending_line': 'print(arr[0])'}


class TestAnswers(unittest.TestCase):

    def test_sort_by_updownvote(self):
        result = sort_by_updownvote(answers=(Answer(id='7098953',
                                 url='https://stackoverflow.com/questions/7098938/nameerror-name-array-is-not-defined-in-python/7098953#7098953',
                                 accepted=False,
                                 score=60,
                                 body='<p>You need to import the <code>array</code> method from the module.</p>\n\n<p><code>from array import array</code></p>\n\n<p><a href="http://docs.python.org/library/array.html" rel="noreferrer">http://docs.python.org/library/array.html</a></p>\n',
                                 author='逆さま',
                                 profile_image='https://www.gravatar.com/avatar/782a7a5f79b342bb12dc0aaae3a0c34d?s=256&d=identicon&r=PG'),),
                                error_info=error_info)

        expected_result = [Answer(id='7098953',
                                 url='https://stackoverflow.com/questions/7098938/nameerror-name-array-is-not-defined-in-python/7098953#7098953',
                                 accepted=False,
                                 score=60,
                                 body='<p>You need to import the <code>array</code> method from the module.</p>\n\n<p><code>from array import array</code></p>\n\n<p><a href="http://docs.python.org/library/array.html" rel="noreferrer">http://docs.python.org/library/array.html</a></p>\n',
                                 author='逆さま',
                                 profile_image='https://www.gravatar.com/avatar/782a7a5f79b342bb12dc0aaae3a0c34d?s=256&d=identicon&r=PG')]

        self.assertEqual(result, expected_result)


    def test_ask_stackoverflow(self):
        result = _ask_stackoverflow("https://api.stackexchange.com/2.2/search?site=stackoverflow&order=desc&sort=relevance&tagged=python&intitle=nameerror+name+is+not+defined&pagesize=3")
        expected_result = Question(id='21122540',
                                   has_accepted='accepted_answer_id',
                                   question_link='https://stackoverflow.com/questions/21122540/input-error-nameerror-name-is-not-defined')

        self.assertEqual(result[0], expected_result)


    def test_ask_google(self):
        result = _ask_google(error_message="NameError: name 'arr' is not defined",
                             n_questions=1)

        expected_result = (Question(id='7098938', has_accepted=None, question_link='https://stackoverflow.com/questions/7098938/nameerror-name-array-is-not-defined-in-python'),)

        self.assertEqual(result, expected_result)


    def test_get_answer_content(self):
        result = _get_answer_content((Question(id='7098938', has_accepted=None, question_link='https://stackoverflow.com/questions/7098938/nameerror-name-array-is-not-defined-in-python'),))
        expected_result = Answer(id='7098953',
                                 url='https://stackoverflow.com/questions/7098938/nameerror-name-array-is-not-defined-in-python/7098953#7098953',
                                 accepted=False,
                                 score=60,
                                 body='<p>You need to import the <code>array</code> method from the module.</p>\n\n<p><code>from array import array</code></p>\n\n<p><a href="http://docs.python.org/library/array.html" rel="noreferrer">http://docs.python.org/library/array.html</a></p>\n',
                                 author='逆さま',
                                 profile_image='https://www.gravatar.com/avatar/782a7a5f79b342bb12dc0aaae3a0c34d?s=256&d=identicon&r=PG')

        self.assertEqual(result[0], expected_result)


if __name__ == "__main__":
    unittest.main()