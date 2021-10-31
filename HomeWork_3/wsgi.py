import datetime
import json


def app_dynamic(env, start_response):
    #print(env)
    data = json.dumps({
        'time': str(datetime.datetime.now()),
        'url': "http://" + env["HTTP_HOST"] + env["RAW_URI"]
    })
    data = bytes(data, 'utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/json"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])


def app_static(env, start_response):
    #print(env)
    with open("public/index.html", "rb") as f:
        data = f.read()
    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
