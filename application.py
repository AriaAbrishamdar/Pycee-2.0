from pycee.answers import get_answers
from pycee.errors import handle_error
from pycee.control import get_error_info
from pycee.utils import parse_args, remove_cache, return_answers

from consolemd import Renderer


def main():

    args = parse_args()

    if args.rm_cache:
        remove_cache()

    error_info = get_error_info(args.file_name)
    query = handle_error(error_info, args)
    so_answers, _, links = get_answers(query, error_info, args)
    result = return_answers(so_answers, links, args)

    # Using renderer to show answers
    renderer = Renderer()
    renderer.render(result)

if __name__ == "__main__":
    main()
