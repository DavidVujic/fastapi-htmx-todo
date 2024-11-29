from .body import body
from .head import head


def html(title: str, header: str, message: str) -> list:
    return [["!DOCTYPE", {"html"}], ["html", head(title), body(header, message)]]
