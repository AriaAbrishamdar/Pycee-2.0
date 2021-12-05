import json

filename = "vote/updowndata.json"

def updowndata(solution_link: str, error_type: str, value: int):
    """
    Create a new item.
    """

    data = {
        "solution_link": solution_link,
        "error_type": error_type,
        "value": value
    }

    return data


def write_json(new_data: dict):
    """
    Save or update vote count in database (updowndata.json).
    """

    with open(filename, 'r+') as file:
        file_data = json.load(file)
        flag = 0

        for x in file_data['data']:
            if new_data['solution_link'] in x['solution_link'] and new_data['error_type'] in x['error_type']:
                print("true")
                flag = 1

                if new_data['value'] == 1:
                    x['value'] = x['value'] + 1

                if new_data['value'] == -1:
                    x['value'] = x['value'] - 1

                with open(filename, 'w') as file:
                    json.dump(file_data, file, indent=4)

                break

        if flag != 1:
            file_data["data"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=2)


def read_json(solution_link: str, error_type:str):
    """
    Read "updowndata.json" to get vote count for the solution.
    """

    with open(filename, 'r+') as file:
        file_data = json.load(file)

        for item in file_data['data']:
            if item['solution_link'] in solution_link and item['error_type'] in error_type:
                return item['value']

    return 0
