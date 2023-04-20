
# APIs:
Flask + Postgresql based API with two apps(listed below), Organized using 'Flask Blueprints'
Geo location enabled data storage/processing using postgis extension 

## 1. Weather
    ### API GET WEATHER OF A PLACE 
    GET -> /weather/?lat=<latitude>&long=<longitude>
## 2. POSTS
    ### ADD POSTS, GET ALL POSTS
    GET | POST -> /posts | POST request should have a json payload like: { "lat": <latitude>, "long": <longitude> } 
    ### GET NEARBY POSTS BASED ON COORDINATES
    GET -> /posts/nearby/?lat=<latitude>&long=<longitude>
    

