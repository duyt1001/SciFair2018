from flask import Flask, render_template, request, jsonify
import os, os.path, sys
from subprocess import run
import time

app = Flask(__name__)

# detectors map the type to the backend program
detectors = {
    "orange":    "anna_color_detector.py",
    "blue":      "anna_color_detector.py",
    "green":     "anna_color_detector.py",
    "purple":    "anna_color_detector.py",
    "circle":    "lookingatshapes.py",
    "rectangle": "lookingatshapes.py",
    "triangle":  "lookingatshapes.py",
    "square":    "lookingatshapes.py",
    "pentagon":    "lookingatshapes.py",
    "all":       "lookingatshapes.py",
    "colormapping": "comparison850and950nma.py"
}

# Default http path will load index.html template
@app.route('/')
@app.route('/index.html')
def index():
    imgs_850 = sorted(os.listdir("static/img/850nm/"))
    imgs_950 = sorted(os.listdir("static/img/950nm/"))
    imgs_visible = sorted(os.listdir("static/img/visible/"))
    imgs_shape = sorted(os.listdir("static/img/shape/"))
    app.logger.debug("imgs_visible: %s", imgs_visible)
    return render_template('index.html', **locals())

# load picture, could be more useful, now seems only 404
@app.route('/load')
@app.route('/loadpicture.html')
def loadpicture():
    reqtype = request.args.get('reqtype', '')
    imgfile = request.args.get('imgfile', '')
    if reqtype in {'visible', '850nm', '950nm'}:
        img = 'static/img/' + reqtype + '/' + imgfile
    else:
        img = 'static/img/' + imgfile
    app.logger.debug('requesting: ' + img)
    if not os.path.isfile(img):
        img = 'static/img/404.jpg'
    else:
        # Add random number to force reloading image
        img = img + '?' + str(int(time.time()))
    return render_template('loadpicture.html', img=img)

# color, morphology, color-mapping, both use this to run backend program
@app.route('/runbackend')
def runbackend():
    color = request.args.get('color', '')
    shape = request.args.get('shape', '')
    colormapping = request.args.get('ircolormapping', '')
    if color:
        if detectors[color]:
            app.logger.debug("python3 " + detectors[color] + " --color " + color)
            run(["python3", detectors[color], "--color", color])
        else:
            pass
    elif shape:
        if detectors[shape]:
            imgshape = "static/img/shape/" + request.args.get('imgfile', '')
            app.logger.debug("python3 " + detectors[shape] + imgshape + shape)
            run(["python3", detectors[shape], "-i", imgshape, "--shape", shape])
        else:
            pass
    elif colormapping:
        image850 = "static/img/850nm/" +request.args.get('select850', '')
        image950 = "static/img/950nm/" +request.args.get('select950', '')
        app.logger.debug ("python3 "+ detectors["colormapping"] + " -i " + image850 + " -j " + image950)
        run("python3 "+ detectors["colormapping"] + " -i " + image850 + " -j " + image950, shell=True)
        #return render_template('loadpicture.html', img='static/img/compare-850-950.png'+ '?' + str(int(time.time())))
    else:
        app.logger.debug ("Neither color nor shape")
    return index()

# Error handling, the happy and cute 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('loadpicture.html', img='static/img/404.jpg'), 404

# http://localhost:5000 or http://127.0.0.1:5000 are entry urls to start
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)