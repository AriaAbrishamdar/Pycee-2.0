from pycee.answers import get_answers
from pycee.errors import handle_error
from pycee.utils import parse_args, remove_cache, return_answers_for_web
from pycee.control import get_error_info_from_traceback
import markdown
import json

from consolemd import Renderer

def create_JSON(so_answers: list, links: list):
    """
    Change the data format of solutions and their links to JSON
    :return: JSON
    """
    data_set = {
        "items": []
    }

    for i in range(0, len(so_answers), 1):
        data = {
            "body": so_answers[i],
            "URL": links[i]
        }
        data_set["items"].append(data)

    return json.dumps(data_set)

def write_json(new_data, filename='updown.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        flag = 0
        for x in file_data['data']:
            if new_data['solution_link'] in x['solution_link'] and new_data['error_type'] in x['error_type'] :
                print("true")
                flag = 1
                if new_data['value'] == 1 :
                    x['value'] = x['value'] + 1
                if new_data['value'] == -1 :
                    x['value'] = x['value'] - 1   
                with open(filename,'w') as file: 
                    json.dump(file_data,file,indent = 4)
                break

        if flag != 1 :    
            file_data["data"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4) 

def updownvote(solution_link : str ,error_type : str , value : int):
    
    data = {
        "solution_link":solution_link,
        "error_type":error_type,
        "value":value
    }
    return data

     
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
        return create_JSON(so_answers, links)

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
#     print(main(_traceback, _code, _n_answers=2, _colored=True, _json=True))
