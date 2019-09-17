#!/usr/bin/python3
"""
Export to CSV
"""
import csv
import requests
import sys


if __name__ == "__main__":

    id_number = sys.argv[1]
    gusers = requests.get('https://jsonplaceholder.typicode.com/users').json()
    gtodos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    add_list = []

    for users in gusers:
        if (users['id'] == int(sys.argv[1])):
            id_number = sys.argv[1]
            user = users.get('username')
            for i in gtodos:
                if (i.get('userId') == int(id_number)):
                    add_list.append([id_number, user,
                                     i.get('completed'),
                                     i.get('title')])

    with open("{}.csv".format(id_number), "wt") as csvfile:
        file = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for entry in add_list:
            file.writerow(entry)
