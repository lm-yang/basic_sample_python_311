import json
import sys
import os 
import flask 

application = flask.Flask(__name__)

@application.route('/')
def hello_world():
    return flask.jsonify({
        'name': 'flaskapp',
        'python_version': sys.version.split(" ", 2)[0],
        'environment': os.environ.copy(),
        'flask_version': flask.__version__,
    })

@application.route('/pre-build')
def pre_build():
    with open("pre-build.txt", "r") as f:
        return flask.jsonify({
            'name': 'flaskapp',
            'python_version': sys.version.split(" ", 2)[0],
            'environment': os.environ.copy(),
            'flask_version': flask.__version__,
            'pre-build': f.read()
        })

@application.route('/build')
def build():
    with open("build.txt", "r") as f:
        return flask.jsonify({
            'name': 'flaskapp',
            'python_version': sys.version.split(" ", 2)[0],
            'environment': os.environ.copy(),
            'flask_version': flask.__version__,
            'build': f.read()
        })

@application.route('/pre-run')
def pre_run():
    with open("pre-run.txt", "r") as f:
        return flask.jsonify({
            'name': 'flaskapp',
            'python_version': sys.version.split(" ", 2)[0],
            'environment': os.environ.copy(),
            'flask_version': flask.__version__,
            'pre-run': f.read()
        })

@application.route('/post-build')
def pre_run():
    if os.path.exists("post-build.txt"):
        with open("post-build.txt", "r") as f:
            return flask.jsonify({
                'name': 'flaskapp',
                'python_version': sys.version.split(" ", 2)[0],
                'environment': os.environ.copy(),
                'flask_version': flask.__version__,
                'post-build': f.read()
            })
    else:
        return flask.jsonify({
            'name': 'flaskapp',
            'python_version': sys.version.split(" ", 2)[0],
            'environment': os.environ.copy(),
            'flask_version': flask.__version__,
            'post-build': 'file not exist'
        })

if __name__ == '__main__':
    port = int(os.environ.get("FLASK_RUN_PORT", 8000))
    application.run(host='0.0.0.0', debug=False, port=port)
