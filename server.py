from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import os
# import kasper sin fil her

# FOR Å RUNNE SERVEREN ER DET BARE Å RUNNE DENNE FILEN. URL DUKKER OPP I TERMINALEN.

UPLOAD_FOLDER = 'uploadedFiles'
ALLOWED_EXTENSIONS = {'prt'}
STATIC_FOLDER = os.path.join('static')

# Initializing varaibles
wielding_gun_nozzle = ''
filename = ''

# Legg til image handler her (png og jpg)

app = Flask(__name__)
app.debug = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STATIC_FOLDER'] = STATIC_FOLDER


@app.route("/", methods=['GET', 'POST'])
def home():
    nozzles = ["Recessed", "Flatten", "Wide", "Custom"]
    if request.method == 'GET':
        return render_template("index.html", nozzles=nozzles)
    if request.method == 'POST':
        wielding_gun_nozzle = (request.form.get('nozzles'))
        print("Type: ", wielding_gun_nozzle)
    return render_template("index.html", nozzles=nozzles, wielding_gun_nozzle=wielding_gun_nozzle)


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("File: ", filename)
        return render_template("uploader.html", filename=filename)

@app.route('/result', methods=['GET', 'POST'])
def show_result():
    if request.method == 'GET':
        image = os.path.join(app.config['STATIC_FOLDER'], 'weldCheck.png')
        return render_template("result.html", image=image, wielding_gun_nozzle=wielding_gun_nozzle, filename=filename)


if __name__ == "__main__":
    app.run()
