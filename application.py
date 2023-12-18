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

def handle(command: str):
    command_content = 'file not exist'
    if os.path.exists(f"{command}.txt"):
        with open(f"{command}.txt", "r") as f:
            command_content = f.read()
    return flask.jsonify({
        'name': 'flaskapp',
        'python_version': sys.version.split(" ", 2)[0],
        'environment': os.environ.copy(),
        'flask_version': flask.__version__,
        f'{command}': command_content
    })
    

@application.route('/pre-build')
def pre_build():
    return handle('pre-build')

@application.route('/build')
def build():
    return handle('build')

@application.route('/post-build')
def post_build():
    return handle('post-build')

@application.route('/pre-run')
def pre_run():
    return handle('pre-run')
    

if __name__ == '__main__':
    port = int(os.environ.get("FLASK_RUN_PORT", 8000))
    application.run(host='0.0.0.0', debug=False, port=port)
