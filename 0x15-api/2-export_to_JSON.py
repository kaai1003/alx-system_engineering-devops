#!/usr/bin/python3
"""display TODOS progress for given employee id"""
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
        json_dict = {id: []}
        for task in todos:
            if task.get("userId") == id:
                json_dict[id].append({"task": task.get("title"),
                                      "completed": task.get("completed"),
                                      "username": user_name})
        filename = str(id) + ".json"
        with open(filename, mode='w') as f:
            json.dump(json_dict, f)
