def meta() -> list:
    charset = ["meta", {"charset": "UTF-8"}]
    viewport = ["meta", {"name": "viewport", "content": "width=device-with, initial-scale=1.0"}]

    return [charset, viewport]


def link(href: str) -> list:
    return ["link", {"rel": "stylesheet", "href": href}]


def script() -> list:
    props = {
        "src": "https://unpkg.com/htmx.org@2.0.0",
        "integrity": "sha384-wS5l5IKJBvK6sPTKa2WZ1js3d947pvWXbPJ1OmWfEuxLgeHcEbjUUA5i9V5ZkpCw",
        "crossorigin": "anonymous",
    }

    return ["script", props]


def head(title: str) -> list:
    css = [link("https://cdn.simplecss.org/simple.min.css"), link("/static/style.css")]

    return ["head", meta(), ["title", title], css, script()]
