from model.todo import Todo

hx_defaults = {"hx-target": "#todos", "hx-swap": "innerHTML"}


def form() -> list:
    props = {"hx-post": "/todos", "hx-on:htmx:after-request": "this.reset()"}
    form_input = ["input", {"type": "text", "name": "todo", "placeholder": "I'd like to..."}]

    return ["form", hx_defaults | props, form_input, ["button", "Create"]]


def text(item: Todo) -> list:
    props = {
        "name": "text",
        "value": item.text,
        "hx-put": f"/todos/{item.id}",
        "hx-trigger": "keyup changed delay:250ms",
    }
    extra = {"style": "text-decoration: line-through", "disabled": "true"} if item.done else {}

    return ["input", hx_defaults | props | extra]


def checkbox(item: Todo) -> list:
    props = {
        "type": "checkbox",
        "hx-post": f"/todos/{item.id}/toggle",
        "title": "Mark todo as not done" if item.done else "Mark todo as done",
    }
    extra = {"checked": "true"} if item.done else {}

    return ["input", hx_defaults | props | extra]


def button(item: Todo) -> list:
    props = {
        "type": "button",
        "value": "❌",
        "hx-post": f"/todos/{item.id}/delete",
        "title": "Delete todo",
    }

    return ["input", hx_defaults | props]


def li(item: Todo) -> list:
    return ["li", text(item), checkbox(item), button(item)]


def todo_list(items: list[Todo]) -> list:
    if not items:
        return ["li", "No todos. Go create some!"]

    return [li(item) for item in items]
