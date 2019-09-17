#!/usr/bin/python3
"""
"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    gusers = requests.get('https://jsonplaceholder.typicode.com/users').json()
    gtodos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    json_list = {}
    file_name = id + ".json"
    add_list = []

    print(file_name)
    for users in gusers:
        if (users.get('id') == int(id)):
            name = users.get('username')
            for i in gtodos:
                new_dict = {}
                if (i.get('userId') == int(id)):
                    new_dict["task"] = i.get('title')
                    new_dict["completed"] = i.get('completed')
                    new_dict["username"] = name
                    add_list.append(new_dict)

    json_list['{}'.format(id)] = add_list

    with open(file_name, mode='w', encoding='utf-8') as file:
        read_file = json.dumps(json_list)
        file.write(read_file)
