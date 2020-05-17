from flask import Flask

def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'

    return resp


def createApp():
    app = Flask(__name__)
    app.after_request(after_request) 


    from loulis import manage_spider
    app.register_blueprint(manage_spider)

    from autoMake import auto_make
    app.register_blueprint(auto_make)

    return app