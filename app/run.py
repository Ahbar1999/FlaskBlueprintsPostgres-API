from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    
    # register blueprints 
    with app.app_context():
        from weather.routes import weather_bp 
        app.register_blueprint(weather_bp, url_prefix='/weather') 
        from posts import __init__, routes  
        app.register_blueprint(routes.posts_bp, url_prefix='/posts')
    return app

app = create_app()
# print registered urls
print(app.url_map)

if __name__ == '__main__':
    app.debug = True
    app.run()
