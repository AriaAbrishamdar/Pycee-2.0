import json

filename = "vote/updowndata.json"

def detail_data(code: str, error: str, ip: str, score: int):
    """
    Create a new detail item.
    score: 1 for upvote and -1 for downvote.
    """

    detail = {
        "code": code,
        "error": error,
        "IP": ip,
        "score": score
    }

    return detail


def updowndata(solution_link: str, error_type: str):
    """
    Create a new item.
    """

    data = {
        "solution_link": solution_link,
        "error_type": error_type,
        "details": []
    }

    return data


def write_json(new_data: dict, new_detail: dict):
    """
    Save or update vote count in database (updowndata.json).
    """

    with open(filename, 'r') as file:
        file_data = json.load(file)

        # Check the new_data is exist or not.
        flag = 0

        for x in file_data['items']:
            if new_data['solution_link'].__eq__(x['solution_link']) and \
                new_data['error_type'].__eq__(x['error_type']):
                flag = 1


                _append = True

                # if the opposite vote exists for the same code, error and IP, remove that vote instead of adding a new vote
                for i in range(len(x['details'])):
                    if ((x['details'][i]['code'] == new_detail['code']) and \
                        (x['details'][i]['error'] == new_detail['error']) and \
                        (x['details'][i]['IP'] == new_detail['IP']) and \
                        (x['details'][i]['score'] == (-new_detail['score']))):
                            del x['details'][i]
                            _append = False
                            break

                # Add detail item
                if (_append):
                    x['details'].append(new_detail)

                break

        if flag != 1:
            # Add new detail item to new data
            new_data['details'].append(new_detail)

            # Add new item to database
            file_data["items"].append(new_data)



    with open(filename, 'w') as file:
        json.dump(file_data, file, indent=4)


def read_json(solution_link: str, error_type:str):
    """
    1. Read "updowndata.json".
    2. Calculate sum of scores in the item with the solution_link and the error_type as value.
    3. Return the value.
    """

    value = 0

    with open(filename, 'r+') as file:
        file_data = json.load(file)

        for item in file_data['items']:
            if item['solution_link'] in solution_link and item['error_type'] in error_type:

                # Calculate the value
                for x in item['details']:
                    value = value + x['score']

                return value

    return value

