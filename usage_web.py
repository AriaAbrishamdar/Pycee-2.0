import os

from pycee.answers import get_answers
from pycee.errors import handle_error
from pycee.utils import parse_args_by_file_name, remove_cache, return_answers
from pycee.inspection import get_error_info_from_traceback, get_file_name


def main(_traceback: str, _code: str, _colored=False):

    # Get file_name from traceback
    file_name = get_file_name(_traceback)

    # Create file path
    file_path = os.path.join("web received content", str(file_name))

    # Create a .py with specified file_name and write the related code to it.
    if file_name:
        f = open("{}".format(file_path), "w")
        f.write(_code)
        f.close()
    else:
        return "Missed file name."

    # Get error information
    error_info = get_error_info_from_traceback(_traceback, file_path)

    args = parse_args_by_file_name([error_info['file']])

    if args.rm_cache:
        remove_cache()

    query, pycee_hint, pydoc_answer = handle_error(error_info, args)
    so_answers, _ = get_answers(query, error_info, args)
    solution = return_answers(so_answers, pycee_hint, pydoc_answer, args, _colored)

    # Remove created .py
    os.remove(file_path)

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
#     print(main(_traceback, _code, _colored=True))
