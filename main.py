from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Teeting": "Loading... Change test final changes to test"}


#Creating a demo todo list
todos = [
    {"id": 1, "title": "Create a todo list", "description": "Create a todo list using FastAPI"},
    {"id": 2, "title": "Learn FastAPI", "description": "Learn FastAPI to create APIs"},
]

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return {"error": "Todo not found"}

@app.post("/todos")
def post_todo(todo: dict):
    todos.append(todo)
    return todos

@app.put("/todos/{todo_id}")
def put_todo_by_id(todo_id: int, todo: dict):
    for i in range(len(todos)):
        if todos[i]["id"] == todo_id:
            todos[i] = todo
            return todos
    return {"error": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo_by_id(todo_id: int):
    for i in range(len(todos)):
        if todos[i]["id"] == todo_id:
            del todos[i]
            return todos
    return {"error": "Todo not found"}

