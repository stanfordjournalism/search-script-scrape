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
    task = {'num': row['Problem No.'], 'url': row['Related URL'],
            'title': row['Title'], 'lines': ""}
    task['link'] = "<i id='task-{num}'></i>{title} <br> <a href='{url}'>[related URL]</a>".format(
            num=task['num'], title=task['title'], url=task['url']
        )
    task['path'] = "scripts/%s.py" % task['num']
    if exists(task['path']):
        lx = len(open(task['path'], encoding = 'utf-8').readlines())
        if lx > 3:
            task['lines'] = "%s lines" % lx
            task['link'] += "&nbsp;<a href='%s'>[script]</a>" % (task['path'])
            done_count += 1

    tasks.append(task)



#############
# store the text to be added to file
tasklines = []
tasklines.append("The repo currently contains scripts for __%s__ of __%s__ tasks:" %
        (done_count, len(tasks)))
tasklines.append(
"""
|          Title          |  Line count |
|-------------------------|-------------|""")

for task in tasks:
    tasklines.append("| {num}. {link} |  {lines} |".format(**task))





## Get the README.md text
lines = []
with open('README.md', 'r') as inf:
    within_tasks = False
    for line in inf.readlines():
        if not within_tasks:
            if 'begintasks' in line:
                within_tasks = True
                lines.append(line)
                lines.extend([t + "\n" for t in tasklines])
            else:
                lines.append(line)
        elif within_tasks:
            if 'endtasks' in line:
                lines.append(line)
                within_tasks = False

with open('README.md', 'w') as outf:
    outf.writelines(lines)


