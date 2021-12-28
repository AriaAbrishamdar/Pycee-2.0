from pycee.answers import get_answers
from pycee.errors import handle_error
from pycee.utils import parse_args, remove_cache, return_answers_for_web
from pycee.control import get_error_info_from_traceback
from vote.updownvote import updowndata, write_json, read_json, detail_data
import markdown
import json

from consolemd import Renderer

def send_updownvote(solution_link: str ,error_type: str, value: int, code: str, error: str, ip: str):
    """
    Save or update new vote count in database.
    """

    # Create a new detail item
    detail_set = detail_data(code, error, ip, value)

    # Create a new data set
    data_set = updowndata(solution_link, error_type)

    # Save or update data set in database
    write_json(data_set, detail_set)


def get_updownvote(solution_link : str ,error_type : str):
    """
    Get vote count from database.
    :return: int
    """
    return read_json(solution_link, error_type)


def create_JSON(so_answers: list, links: list, error_info: dict):
    """
    Change the data format of solutions and their links to JSON
    :return: JSON
    """
    data_set = {
        "items": []
    }

    for i in range(0, len(so_answers), 1):

        ans = ""
        # ans += "\n\n**{}**\n\n**Solution {}:**\n\n".format('=' * 40 ,i + 1)
        ans += '<hr style="height:6px;color:gray;background-color:gray">'
        ans += '**Solution {}:**\n'.format(i + 1)

        for a in so_answers[i]:
            ans += str(a)

        ans += "\n"
        ans = markdown.markdown(ans)
        ans = ans.replace("<p>",  '<p style="font-size:18px;">')

        link = '<p><b>\nLink: <a href="{}">{}</a>\n\n\n</b></p>'.format(links[i], links[i])
        link = link.replace("<p>",  '<p style="font-size:18px;">')


        data = {
            "body": ans,
            "link_text": link,
            "link": links[i],
            "error_type": error_info["type"],
            "score": get_updownvote(link , error_info["type"]),
        }
        data_set["items"].append(data)

    return json.dumps(data_set)


def main(_traceback: str, _code: str, _n_answers=0, _colored=False, _json=True):

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

    if _json:
        return create_JSON(so_answers, links, error_info)

    else:
        solution = return_answers_for_web(so_answers, links, args)


        # Check _colored param
        renderer = Renderer()
        if _colored:
            return renderer.render(solution)

        else:
            #solution = "{}\n\n{}\n\n".format(40*'=', 40*'=') + solution
            solution = markdown.markdown(solution)
            solution = solution.replace("<p>",  '<p style="font-size:18px;">')
            return solution


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
#     print(main(_traceback, _code, _n_answers=10, _colored=True, _json=True))
