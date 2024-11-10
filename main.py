from typing import Annotated, Union

from fastapi import FastAPI, Form, Header, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from python_hiccup.html import render

import content
from model.todo import Todo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

todos = []


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    title = "FastAPI + HTMLX"
    data = render(content.html(title=title, header=title, message="Let's create some todos."))
    return HTMLResponse(content=data)


@app.get("/todos", response_class=HTMLResponse)
async def list_todos(request: Request, hx_request: Annotated[Union[str, None], Header()] = None):
    if hx_request:
        data = render(content.todo_list(todos))
        return HTMLResponse(content=data)

    return JSONResponse(content=jsonable_encoder(todos))


@app.post("/todos", response_class=HTMLResponse)
async def create_todo(request: Request, todo: Annotated[str, Form()]):
    todos.append(Todo(todo))
    data = render(content.todo_list(todos))
    return HTMLResponse(content=data)


@app.put("/todos/{todo_id}", response_class=HTMLResponse)
async def update_todo(request: Request, todo_id: str, text: Annotated[str, Form()]):
    for index, todo in enumerate(todos):
        if str(todo.id) == todo_id:
            todo.text = text
            break

    data = render(content.todo_list(todos))
    return HTMLResponse(content=data)


@app.post("/todos/{todo_id}/toggle", response_class=HTMLResponse)
async def toggle_todo(request: Request, todo_id: str):
    for index, todo in enumerate(todos):
        if str(todo.id) == todo_id:
            todos[index].done = not todos[index].done
            break

    data = render(content.todo_list(todos))
    return HTMLResponse(data)


@app.post("/todos/{todo_id}/delete", response_class=HTMLResponse)
async def delete_todo(request: Request, todo_id: str):
    for index, todo in enumerate(todos):
        if str(todo.id) == todo_id:
            del todos[index]
            break

    data = render(content.todo_list(todos))
    return HTMLResponse(data)
