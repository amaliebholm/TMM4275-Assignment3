from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import os
from os import listdir
# import kasper sin fil her

# FOR Å RUNNE SERVEREN ER DET BARE Å RUNNE DENNE FILEN. URL DUKKER OPP I TERMINALEN.

UPLOAD_FOLDER = 'uploadedFiles'
ALLOWED_EXTENSIONS = {'prt'}
STATIC_FOLDER = os.path.join('static')

# Initializing varaibles
global wielding_gun_nozzle
global filename
wielding_gun_nozzle = ''
filename = ''

# Legg til image handler her (png og jpg)

app = Flask(__name__)
app.debug = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STATIC_FOLDER'] = STATIC_FOLDER


@app.route("/", methods=['GET', 'POST'])
def home():
    nozzles = ["Recessed", "Flush", "Adjustable", "Protruding"]
    if request.method == 'GET':
        return render_template("index.html", nozzles=nozzles)
    if request.method == 'POST':
        wielding_gun_nozzle = (request.form.get('nozzles'))
        print("Type: ", wielding_gun_nozzle)
        write_to_File(wielding_gun_nozzle)
    return render_template("index.html", nozzles=nozzles, wielding_gun_nozzle=wielding_gun_nozzle)


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        oldname = file.filename
        file.filename = "weldingModel.prt"
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("File: ", filename)
        return render_template("uploader.html", filename=oldname)


@app.route('/result', methods=['GET', 'POST'])
def show_result():
    if request.method == 'GET':
        image = os.path.join(app.config['STATIC_FOLDER'], 'weldCheck.png')
        filename = request.args.get('file')
        wielding_gun_nozzle = request.args.get('nozzle')
        return render_template("result.html", image=image, wielding_gun_nozzle=wielding_gun_nozzle, filename=filename)


def write_to_File(nozzle):
    diameter = 0.0
    if nozzle == 'Protruding':
        diameter = 25
        print("Diameter set to ", diameter)
    elif nozzle == 'Flush':
        diameter = 30
        print("Diameter set to ", diameter)
    elif nozzle == 'Adjustable':
        diameter = 26
        print("Diameter set to ", diameter)
    elif nozzle == 'Recessed':
        diameter = 19
        print("Diameter set to ", diameter)

    if diameter != 0.0:
        with open('variables.txt', 'w') as f:
            f.write(str(diameter))
            f.close()
        return

    else:
        pass


if __name__ == "__main__":
    app.run()
