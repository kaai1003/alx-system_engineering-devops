#!/usr/bin/python3
"""display TODOS progress for given employee id"""
import csv
import json
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) == 2:
        try:
            id = int(sys.argv[1])
        except ValueError:
            print("Script Argument should be int")
            exit(-1)
        # request user informations
        url_u = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        r_user = requests.get(url_u)
        user = r_user.json()
        user_name = user.get("username")
        # request TODO tasks of user
        url_t = "https://jsonplaceholder.typicode.com/todos"
        r_todos = requests.get(url_t)
        todos = r_todos.json()
        list_tasks = []
        for task in todos:
            if task.get("userId") == id:
                list_tasks.append([task.get("userId"),
                                   user_name,
                                   task.get("completed"),
                                   task.get("title")])
        filename = str(id) + ".csv"
        with open(filename, mode='w') as f:
            w = csv.writer(f, delimiter=',',
                           quotechar='"',
                           quoting=csv.QUOTE_ALL)
            for line in list_tasks:
                w.writerow(line)
