import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/Mes_Services')
def Mes_services():
    return flask.render_template('Mes_Services.html')

@app.route('/Mes_compétences')
def Mes_compétences():
    return flask.render_template('Mes_competences.html')


if __name__ == '__main__':  
    app.run(debug=True, port=8080)