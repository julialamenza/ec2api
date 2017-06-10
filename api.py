# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

from bottle import route, run, request, error
from api_lib import instance_create, instance_info, instance_terminate


@error(403)
def error403(error):
    """Return message."""
    return 'Sorry. This is forbidden to you.'


@error(404)
def error404(error):
    """Return message."""
    return 'Sorry. There is nothing here to you.'


@error(405)
def error405(error):
    return 'Sorry. There is nothing here to you.'


@route('/healthcheck')
def healthcheck():
    return 'OK'

       

@route('/api/create', method='POST')
def api_create_instance():

    instances = instance_create(
        region_name=request.forms.get("region_name"),
        image_id=request.forms.get("image_id"),
        min_count=request.forms.get("min_count"),
        max_count=request.forms.get("max_count"),
        key_name=request.forms.get("key_name"),
        instance_type=request.forms.get("instance_type")
    )
    status = {"Success": True, "InstanceID": instances[0].id}

    return status


@route('/api/info/<region>', method='GET')
def api_instance_info(region):

    instances = instance_info(region)

    return {'instancias': instances}


@route('/api/terminate', method='POST')
def api_instance_terminate():

    instance = instance_terminate(
        region_name=request.json.get("region_name"),
        instance_id=request.json.get("instance_id")
    )
    status = {"Sucess": True, "InstancesRemove": instance}

    return status


#Form for user

@route('/create') 
def login():
    return '''
        <form action="/api/create" method="post">
            Region Name: <input name="region_name" type="text" />
            Image ID: <input name="image_id" type="text" />
            Min Count: <input name="min_count" type="int" />
            Max Count: <input name="max_count" type="int" />
            Key Name: <input name="key_name" type="name" />
            Image Type: <input name="instance_type" type="text" />
            <input value="Create" type="submit" />
        </form>'''



run(host='0.0.0.0', port=8080, server='gevent')
