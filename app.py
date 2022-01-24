"""
John Doe's Flask API.
"""



from flask import Flask,abort,send_from_directory
import os
import configparser

app = Flask(__name__)

@app.route("/<path:request>")
def hello(request):
    if ".." in request or "~" in request:
        abort(403)
    filePath = "./pages/" + request 
    containsFile = os.path.isfile(filePath)
    if containsFile == True:
        return send_from_directory('pages/', request), 200
    else:
        abort(404)

@app.errorhandler(403)
def error403(e):
    return send_from_directory("pages/", "403.html"), 403

@app.errorhandler(404)
def error404(e):
    return send_from_directory("pages/","404.html"), 404

def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break
    if config_path is None:
        raise RunTimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

config = parse_config(["credentials.ini", "default.ini"])
if __name__ == "__main__":
    app.run(debug=config["SERVER"]["DEBUG"], host='0.0.0.0', port=config["SERVER"]["PORT"])
