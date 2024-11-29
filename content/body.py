from .todos import form


def body(header: str, message: str) -> list:
    ul = ["ul#todos", {"hx-get": "/todos", "hx-swap": "innerHTML", "hx-trigger": "load"}]
    main = [["section", form()], ["section", ["h2", "Todos"], ul]]

    return ["body", ["header", ["h1", header], ["p", message]], ["main", main]]
