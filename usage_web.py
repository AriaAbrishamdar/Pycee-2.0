from pycee.answers import get_answers
from pycee.errors import handle_error
from pycee.utils import parse_args_by_file_name, remove_cache, return_answers
from pycee.inspection import get_error_info_from_traceback

def main(traceback):

    error_info = get_error_info_from_traceback(traceback)

    args = parse_args_by_file_name([error_info['file']])

    if args.rm_cache:
        remove_cache()

    query, pycee_hint, pydoc_answer = handle_error(error_info, args)
    so_answers, _ = get_answers(query, error_info, args)
    solution = return_answers(so_answers, pycee_hint, pydoc_answer, args)

    return solution


# Uncomment to test main function
# if __name__ == "__main__":
#
#     _traceback = """Traceback (most recent call last):
#   File "example_code.py", line 2, in <module>
#     print(arr[0])
# IndexError: list index out of range"""
#
#     print(main(_traceback))
