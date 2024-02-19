#!/usr/bin/python3
"""
Gather data from an API
then export it in json format
"""
import json
import requests
import sys


if __name__ == "__main__":
    file_name = 'todo_all_employees.json'
    todo_dict = {}
    for id in range(1, 11):
        url = f"https://jsonplaceholder.typicode.com/users/{id}"
        req = requests.get(url).json()
        tasks_url = url + "/todos"
        tasks = requests.get(tasks_url).json()

        dict_id = str(req.get('id'))
        task_infos = []
        for task in tasks:
            t_dict = {'username': req.get('username'),
                      'task': task.get('title'),
                      'completed': task.get('completed')}
            task_infos.append(t_dict)
            todo_dict[dict_id] = task_infos

    with open(file_name, 'w') as f:
        json.dump(todo_dict, f)
