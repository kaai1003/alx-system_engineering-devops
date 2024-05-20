#!/usr/bin/python3
"""display TODOS progress for given employee id"""
import json
import sys
import urllib.request


if __name__ == "__main__":

    if len(sys.argv) == 2:
        try:
            id = int(sys.argv[1])
        except ValueError:
            print("Script Argument should be int")
            exit(-1)
        # request user informations
        url_u = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        r = urllib.request.urlopen(url_u)
        user = json.loads(r.read())
        user_name = user.get("name")
        # request TODO tasks of user
        url_t = "https://jsonplaceholder.typicode.com/todos"
        r = urllib.request.urlopen(url_t)
        todos = json.loads(r.read())
        list_tasks = []
        task_count = 0
        completed_tasks = 0
        for todo in todos:
            if todo.get("userId") == id:
                task_count += 1
                if todo.get("completed") is True:
                    list_tasks.append(todo.get("title"))
                    completed_tasks += 1
        print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                              completed_tasks,
                                                              task_count))
        for title in list_tasks:
            print("\t {}".format(title))
