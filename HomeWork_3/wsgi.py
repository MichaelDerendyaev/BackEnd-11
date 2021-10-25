def app(environ, start_response):
    with open("public/Static.json", "rb") as f:
        data = f.read()
    start_response("200 OK", [
        ("Content-Type", "json"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
