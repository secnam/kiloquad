import os

from luxon import register_resource
from luxon import g
from luxon import GetLogger

log = GetLogger(__name__)

@register_resource('GET', '/v1/objects')
def objects(req, resp):
    pass

@register_resource('GET', '/v1/object/{id}')
def object(req, resp, id):
    path = g.config.get('storage', 'path', fallback='/tmp').rstrip('/')
    
    with open(path + '/' + id, 'rb') as file:
        return file.read()

@register_resource('POST', '/v1/object/{id}')
def store(req, resp, id):
    path = g.config.get('storage', 'path', fallback='/tmp').rstrip('/')

    payload = req.read()

    with open(path + '/' + id, 'bw') as file:
        file.write(payload)

    return payload

@register_resource('DELETE', '/v1/object/{id}')
def delete(req, resp, id):
    path = g.config.get('storage', 'path', fallback='/tmp').rstrip('/')

    os.remove(path + '/' + id)



