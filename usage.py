from pycee.answers import get_answers
from pycee.errors import handle_error
from pycee.inspection import get_error_info
from pycee.utils import parse_args, remove_cache, print_answers, return_answers


def main():

    args = parse_args()

    if args.rm_cache:
        remove_cache()

    error_info = get_error_info(args.file_name)
    query = handle_error(error_info, args)
    so_answers, _ = get_answers(query, error_info, args)
    print_answers(so_answers, args)


if __name__ == "__main__":
    main()
