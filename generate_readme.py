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
tasks = csv.DictReader(txt.splitlines())
print(
"""
| Title  |  Line count |
|--------|-------------|
""")

done_count = 0;

for row in sorted(tasks, key = lambda r: int(r['Problem No.'])):
    task = {'num': row['Problem No.'],
            'title': row['Title']}
    task['path'] = "scripts/%s.py" % task['num']
    if exists(task['path']):
        task['lines'] = len(open(task['path'], encoding = 'utf-8').readlines())
        done_count += 1
    else:
        task['lines'] = "Not in repo."

    print("| {num}. [{title}]({path})  |  {lines} |".format(**task))


print("# done: ", done_count)
