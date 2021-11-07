"""Contains all the logic that handles code errors."""
import re
from typing import List, Union
from argparse import Namespace

from slugify import slugify

from .utils import SEARCH_URL
from .utils import (
    SINGLE_QUOTE_CHAR,
    SINGLE_SPACE_CHAR,
    EMPTY_STRING,
)


def handle_error(error_info: dict, cmd_args: Namespace) -> tuple:
    """Process the incoming error as needed and outputs three possible answer.
    output:
    query: an URL containing an stackoverflow query about the error.
    """

    error_type = error_info["type"]
    error_message = error_info["message"]

    if error_type == "SyntaxError":
        query = handle_syntax_error(error_message)

    elif error_type == "TabError":
        query = handle_tab_error(error_message)

    elif error_type == "IndentationError":
        query = handle_indentation_error(error_message)

    elif error_type == "IndexError":
        query = handle_index_error(error_message)

    elif error_type == "ModuleNotFoundError":
        query = handle_module_not_found_error(error_message)

    elif error_type == "TypeError":
        query = handle_type_error(error_message)

    elif error_type == "KeyError":
        query = handle_key_error(error_message)

    elif error_type == "AttributeError":
        query = handle_attr_error(error_message)

    elif error_type == "NameError":
        query = handle_name_error(error_message)

    elif error_type == "ZeroDivisionError":
        query = handle_zero_division_error(error_message)

    else:
        query = url_for_error(error_message)  # default query

    query = set_pagesize(query, cmd_args.n_questions) if query else None

    if cmd_args.dry_run:
        print(query)
        exit()

    return query


def handle_key_error(error_message: str) -> str:
    """ Directly asks Stackoverflow for similar errors. """

    error = slugify(error_message, separator="+")
    return url_for_error(error)


def handle_name_error(error_message: str) -> str:
    """Process an NameError by removing the variable name.
    By doing this the default error can be search without interference
    of the variable name, which does not add to the problem.

    example:
    input:
        "NameError: name 'a' is not defined"
    output:
        "NameError: name is not defined"
    """
    return url_for_error(remove_quoted_words(error_message))


def handle_module_not_found_error(error_message: str) -> str:
    """Handling ModuleNoutFoundError is quite simple as most of well known packages
    already have questions on ModuleNotFoundError solved at stackoverflow"""

    message = error_message.replace("ModuleNotFoundError", EMPTY_STRING)
    return url_for_error(message)


def handle_index_error(message: str) -> str:
    """Process an IndexError."""

    message = slugify(message, separator="+")

    return url_for_error(message)


def handle_attr_error(error_message: str) -> str:
    """Process an AttributeError by directly asking StackOverflow
    about the error message."""

    error = slugify(error_message, separator="+")
    return url_for_error(error)


def handle_indentation_error(error_message: str) -> str:
    """Process an IndentationError."""

    message = remove_exception_from_error_message(error_message)
    return url_for_error(message)


def handle_syntax_error(error_message: str) -> Union[str, None]:
    """Process a SyntaxError """

    # if a generic SyntaxError happens
    # it's quite tricky to catch the right offending line
    if error_message == "SyntaxError: invalid syntax":
        return None
    else:
        error = slugify(error_message, separator="+")
        return url_for_error(error)


def handle_tab_error(error_message: str) -> str:
    """Process an TabError."""
    message = remove_exception_from_error_message(error_message)
    return url_for_error(message)


def handle_type_error(error_message: str) -> str:
    """Process an TypeError."""

    hint1 = "the first argument must be callable"
    hint2 = "not all arguments converted during string formatting"
    if hint1 in error_message:
        message = "must have first callable argument"
    elif hint2 in error_message:
        message = remove_exception_from_error_message(error_message)
    else:
        return url_for_error(error_message)

    message = slugify(message, separator="+")

    return url_for_error(message)


def handle_zero_division_error(error_message: str) -> str:
    """Process an ZeroDivisionError"""

    message = remove_exception_from_error_message(error_message)
    return url_for_error(message)


def set_pagesize(query: str, pagesize: int) -> str:
    """Set the number of questions we want from Stackoverflow."""
    return query + f"&pagesize={pagesize}"


def get_query_params(error_message: str) -> str:
    """Prepares the query to include necessary filters and meet URL format."""

    error_message_slug = slugify(error_message, separator="+")
    order = "&order=desc"
    sort = "&sort=relevance"
    python_tagged = "&tagged=python"
    intitle = f"&intitle={error_message_slug}"

    return order + sort + python_tagged + intitle


def url_for_error(error_message: str) -> str:
    """Build a valid search url."""

    return SEARCH_URL + get_query_params(error_message)


def get_quoted_words(error_message: str) -> List[str]:
    """Extract words surrounded by single quotes.
    Example:
    input: "AttributeError: 'int' object has no attribute 'append'"
    output: ['int', 'append']
    """
    return error_message.split(SINGLE_QUOTE_CHAR)[1::2]


def remove_exception_from_error_message(error_message: str) -> str:
    """Removes the exception error from the error message.
    Example:
    input: "AttributeError: 'int' object has no attribute 'append'"
    output: "'int' object has no attribute 'append'"
    """
    return error_message.split(SINGLE_SPACE_CHAR, 1)[1]


def remove_quoted_words(error_message: str) -> str:
    """Removes quoted words from an error message.
    Example:
    input: "NameError: name 'a' is not defined"
    output: "NameError: name is not defined"
    """
    return re.sub(r"'.*?'\s", EMPTY_STRING, error_message)
