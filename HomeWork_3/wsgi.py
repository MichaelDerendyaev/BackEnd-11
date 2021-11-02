import datetime
import json


def app(env, start_response):
    #print(env)
    data = json.dumps({
        'time': str(datetime.datetime.now()),
        'url': "http://" + env["HTTP_HOST"] + env["RAW_URI"]
    })
    data = bytes(data, 'utf-8')
    start_response("200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
