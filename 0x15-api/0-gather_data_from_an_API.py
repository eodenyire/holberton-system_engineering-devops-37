#!/usr/bin/python3
"""Returns information about TODO list progress"""
import requests
import sys

if __name__ == "__main__":

    gusers = requests.get('https://jsonplaceholder.typicode.com/users').json()
    gtodos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    total = 0
    completed = 0
    add_list = []

    for i in gtodos:
        if (i['userId'] == int(sys.argv[1])):
            total += 1
            if i['completed'] is True:
                add_list.append(i.get('title'))
                completed += 1

    for users in gusers:
        if (users['id'] == int(sys.argv[1])):
            print("Employee {} is done with tasks({}/{}):".
                  format((users['name']), completed, total))

    for i in add_list:
        print("\t{}".format(i))
