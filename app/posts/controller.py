import json
from .models import Post
from flask import request
from shapely import wkb, Point
from .__init__ import session
from geoalchemy2 import functions 


def get_posts():
    result = session.query(Post).all()
    return json.dumps([obj.serialize() for obj in result])

def submit_post():
    print('Recieved submit request')
    print(request)
    data = request.get_json()
    print('data',data) 
    session.add(Post(message=data['message'], location=f'POINT( {data["location"]["lat"]} {data["location"]["long"]} )'))
    session.commit()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

# HINT: https://stackoverflow.com/questions/20803878/geoalchemy2-query-all-users-within-x-meteres
def get_nearby_posts():     
    # convert loc to wkb_element before passing
    # https://gis.stackexchange.com/questions/401862/python-shapely-to-convert-2-columns-to-wkb 
    lat = request.args.to_dict()['lat']
    long = request.args.to_dict()['long']
    wkb_loc = wkb.dumps(Point(lat, long))
    distance = 1; 
    result = session.query(Post).filter(functions.ST_DFullyWithin(Post.location, wkb_loc, distance)).all()
    return json.dumps([obj.serialize() for obj in result])


