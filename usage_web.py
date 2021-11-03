from pycee.answers import get_answers
from pycee.errors import handle_error
from pycee.utils import parse_args, remove_cache, return_answers
from pycee.inspection import get_error_info_from_traceback

from consolemd import Renderer



def main(_traceback: str, _code: str, _n_answers=0, _colored=False):

    # Get error information
    error_info = get_error_info_from_traceback(_traceback, _code)

    # Create parseargs
    if _n_answers:
        args = parse_args(args=['-a', str(_n_answers), error_info['file']])
    else:
        args = parse_args(args=[error_info['file']])

    if args.rm_cache:
        remove_cache()

    query = handle_error(error_info, args)
    so_answers, _, links = get_answers(query, error_info, args)
    solution = return_answers(so_answers, links, args)

    # Check _colored param
    renderer = Renderer()
    if _colored:
        return renderer.render(solution)

    else:
        return print(solution)


# Uncomment to test main function
# if __name__ == "__main__":
#
#     _traceback = """Traceback (most recent call last):
#   File "example_code.py", line 1, in <module>
#     print(arr[0])
# NameError: name 'arr' is not defined"""
#
#     _code = """print(arr[0])"""
#
#     main(_traceback, _code, _n_answers=2, _colored=True)
