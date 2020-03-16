from flask import Flask
from random import random
import logging
from flask import request
from flask import render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def dong():
    return render_template('dong.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(request.form['fname'])
    logging.debug(request.form['salary'])
    name = request.form['fname']
    salary = request.form['salary']
    if name == "uttejh":
        logging.debug("reddy")
        return render_template('rest.html', employee=name + ' reddy', hoursofwork= str(str((int(salary) * 100)) + ' SEK'))
    elif name == "ashik":
        logging.debug("doors")
        return render_template('rest.html', employee=name + ' doors', hoursofwork= str(str((int(salary) * 100)) + ' SEK'))
    else:
        logging.debug("Employee details are wrong")
        return render_template('rest.html', employee= "unknown", hoursofwork= "not applicable")


if __name__ == '__main__':
    app.run(debug=True)
