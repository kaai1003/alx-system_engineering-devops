#!/usr/bin/python3
"""display TODOS progress for given employee id"""
import json
import requests
import sys


if __name__ == "__main__":

    # request user informations
    url_u = "https://jsonplaceholder.typicode.com/users"
    r_user = requests.get(url_u)
    users = r_user.json()
    # request TODO tasks of user
    url_t = "https://jsonplaceholder.typicode.com/todos"
    r_todos = requests.get(url_t)
    todos = r_todos.json()
    json_dict = {}
    for user in users:
        user_id = user.get("id")
        json_dict[user_id] = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                json_dict[user_id].append({"username": user.get("username"),
                                           "task": task.get("title"),
                                           "completed": task.get("completed")})
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as f:
        json.dump(json_dict, f)
