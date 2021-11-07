"""Some data to be kept apart from application logic."""

import argparse
from collections import namedtuple
import glob
import os
import pathlib
import sys


def parse_args(args=sys.argv[1:]):
    """A simple argparse to be used when pycee is executed as a script."""

    parser = argparse.ArgumentParser("pycee2", description="Pycee is a tool to provide user friendly error messages.")
    parser.add_argument(
        "file_name",
        type=str,
        help="Path to the script that contains the error",
    )
    parser.add_argument(
        "-q",
        metavar="--n-questions",
        type=int,
        choices=range(1, 6),
        default=3,
        dest="n_questions",
        help="Number of questions to retrieve from Stackoverflow",
    )
    parser.add_argument(
        "-a",
        metavar="--n-answers",
        type=int,
        choices=range(1, 5),
        default=3,
        dest="n_answers",
        help="Number of answers to display",
    )
    parser.add_argument(
        "-g",
        "--from-google-search",
        dest="google_search_only",
        action="store_true",
        default=False,
        help="Retrieve questions only from Google search engine",
    )
    parser.add_argument(
        "-s",
        "--stackoverflow-answer",
        dest="show_pycee_hint",
        action="store_false",
        default=True,
        help="Output only StackOverflow answers for the error",
    )
    parser.add_argument(
        "-p",
        "--pycee-hint",
        dest="show_so_answer",
        action="store_false",
        default=True,
        help="Output only pycee hint for the error",
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Return only the stackoverflow query. For test purposes",
    )
    parser.add_argument(
        "-rm",
        "--remove-cache",
        dest="rm_cache",
        action="store_true",
        default=False,
        help="Remove all local cache files",
    )
    parser.add_argument(
        "-f",
        "--no-cache",
        dest="cache",
        action="store_false",
        default=True,
        help="Force API requests by skipping any local caches",
    )

    return parser.parse_args(args)


def remove_cache():
    """Util to remove the cache files, which can be located at two different places
    depending if pycee is running as a installed package or as a cloned repository"""

    installed_module_path = pathlib.Path(__file__).parent.absolute()
    package_cache = glob.glob(os.path.join(installed_module_path, "*.cache*"))
    local_cache = glob.glob("pycee/*.cache*")
    files = package_cache + local_cache
    print("Cache removed!\nPlease run pycee again without -rm or --remove-cache argument to get your answers")
    # excecvp replace the current process
    # This is currently necessary because filecache package
    # wouldn't let me delete all cache files on the main process
    # -f so not found files won't polute the terminal
    os.execvp("rm", ["rm", "-f"] + files)
    # after execv vp finishes executing rm it exits


def return_answers(so_answers, links, args):
    """ Hide the logic of printing answers from the usage example """

    result = ""

    if args.show_so_answer:

        if not so_answers:
            result += "Pycee couldn't find answers for the error on Stackoverflow.\n"

        else:
            for i, answer in enumerate(so_answers):
                result += "\n\n**{}**\n\n**Solution {}:**\n\n".format('=' * 40 ,i + 1)
                result += answer
                result += "\n"

    result += "\n\n**{}**\n\n".format('=' * 40)
    result += "**Links:**\n"

    for i in range(len(links)):
        result += "{}. {}\n".format(i + 1, links[i])

    return result


def return_answers_for_web(so_answers, links, args):
    """ Hide the logic of printing answers from the usage example """

    result = ""

    if args.show_so_answer:

        if not so_answers:
            result += "Pycee couldn't find answers for the error on Stackoverflow.\n"

        else:
            for i, answer in enumerate(so_answers):
                result += "\n\n**{}**\n\n**Solution {}:**\n\n".format('=' * 40 ,i + 1)
                result += answer
                result += "\n"

    result += "\n\n**{}**\n\n".format('=' * 40)
    result += "**Links:**\n"
    for i in range(len(links)):

        result += '\n{}. <a href="{}">{}</a>\n'.format(i + 1, links[i], links[i])

    return result


# These are some constants we use throughout the codebase
SINGLE_QUOTE_CHAR = "'"
DOUBLE_QUOTE_CHAR = '"'
SINGLE_SPACE_CHAR = " "
EMPTY_STRING = ""
COMMA_CHAR = ","

BASE_URL = "https://api.stackexchange.com/2.2"
SEARCH_URL = BASE_URL + "/search?site=stackoverflow"
ANSWERS_URL = BASE_URL + "/questions/<id>/answers?site=stackoverflow" + "&filter=withbody" + "&order=desc" + "&sort=votes"

# A list of all standard exeptions
BUILTINS = dir(sys.modules["builtins"])

# namedtuples to represent simple objects
Question = namedtuple("Question", ["id", "has_accepted"])
Answer = namedtuple("Answer", ["id", "accepted", "score", "body", "author", "profile_image"])
