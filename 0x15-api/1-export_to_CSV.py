#!/usr/bin/python3
"""
Gather data from an API
then export to CSV
"""
import csv
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

    field_names = ['USER_ID', 'USERNAME',
                   'TASK_COMPLETED_STATUS',
                   'TASK_TITLE']

    dictt = {'USER_ID': str(req.get('id')),
             'USERNAME': str(req.get('username'))}

    file_name = dictt['USER_ID'] + '.csv'
    with open(file_name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=field_names,
                                quoting=csv.QUOTE_ALL)

        for task in tasks:
            dictt['TASK_COMPLETED_STATUS'] = str(task.get('completed'))
            dictt['TASK_TITLE'] = str(task.get('title'))
            writer.writerow(dictt)
