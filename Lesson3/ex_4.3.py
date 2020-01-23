import json
import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
todos_by_user = {}
for todo in todos:
    try:
        if todo['completed']:
            todos_by_user[todo['userId']] += 1
    except KeyError:
        todos_by_user[todo['userId']] = 1
print(todos_by_user)