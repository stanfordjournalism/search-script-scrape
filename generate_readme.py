#!/usr/bin/python3
"""
This script reads from the Google Doc of tasks and generates
the titles of the tasks, linked to the appropriate file, and this
(Markdown) text can be pasted into the README.md file
"""
import csv
import requests
from os.path import exists
GDOC_URL = 'https://docs.google.com/spreadsheets/d/1JbY_-g9MkGH78Rta0PnE6D8rG8T-wdKGsMa3kAC3bDs/export?format=csv&gid=0'

txt = requests.get(GDOC_URL).text
rows = csv.DictReader(txt.splitlines())



done_count = 0;
tasks = []
for row in sorted(rows, key = lambda r: int(r['Problem No.'])):
    task = {'num': row['Problem No.'],
            'title': row['Title'], 'lines': ""}
    task['path'] = "scripts/%s.py" % task['num']
    if exists(task['path']):
        lx = len(open(task['path'], encoding = 'utf-8').readlines())
        if lx > 3:
            task['lines'] = "%s lines" % lx
            task['title'] = "[%s](%s)" % (task['title'], task['path'])
            done_count += 1
    tasks.append(task)
#############
# print stuff out
print("The repo currently contains scripts for __%s__ of __%s__ tasks:" %
        (done_count, len(tasks)))
print(
"""
|          Title          |  Line count |
|-------------------------|-------------|""")

for task in tasks:
    print("| {num}. {title} |  {lines} |".format(**task))






