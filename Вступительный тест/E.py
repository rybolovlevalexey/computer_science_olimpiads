import requests
import json


def dwarf_pest(port, host, **kwargs):
    response = requests.get(f'http://{host}{port}')
    if kwargs['place'] in response:
        res = dict()
        for key, value in kwargs.items():
            if key == 'place':
                continue
            res[key] = value
        response[kwargs['place']].append(res)
    else:
        res = dict()
        for key, value in kwargs.items():
            if key == 'place':
                continue
            res[key] = value
        response[kwargs['place']] = [res]
    return json.dumps(response)
