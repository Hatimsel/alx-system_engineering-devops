#!/usr/bin/python3
"""
Gather data from an API
then export to JSON
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./file_name id")
    id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    req = requests.get(url).json()
    tasks_url = url + "/todos"
    tasks = requests.get(tasks_url).json()

    completed_tasks = []
    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task.get('title'))

    dict_id = str(req.get('id'))
    dictt = {}
    task_infos = []

    file_name = str(id) + '.json'
    with open(file_name, 'w') as f:
        for task in tasks:
            t_dict = {'task': task.get('title'),
                      'completed': task.get('completed'),
                      'username': req.get('username')}
            task_infos.append(t_dict)
        dictt[dict_id] = task_infos
        json.dump(dictt, f)
