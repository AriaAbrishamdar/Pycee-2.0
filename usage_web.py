from pycee.answers import get_answers
from pycee.errors import handle_error
from pycee.utils import parse_args, remove_cache, return_answers
from pycee.inspection import get_error_info_from_traceback


def main(_traceback: str, _code: str, _colored=False):

    # Get error information
    error_info = get_error_info_from_traceback(_traceback, _code)

    # Create parseargs
    args = parse_args(args=[error_info['file']])

    if args.rm_cache:
        remove_cache()

    query = handle_error(error_info, args)
    so_answers, _ = get_answers(query, error_info, args)
    solution = return_answers(so_answers, args, _colored)

    return solution


# Uncomment to test main function
# if __name__ == "__main__":
#
#     _traceback = """Traceback (most recent call last):
#   File "ur_name.py", line 2, in <module>
#     print(arr[0])
# IndexError: list index out of range"""
#
#     _code = """arr = []
# if arr[0]:
#     print(arr[0])"""
#
#     print(main(_traceback, _code))
