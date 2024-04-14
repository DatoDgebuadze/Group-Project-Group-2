from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html', app_name='Our ML Group project')


@app.route('/about')
def about():
    return render_template('about.html', app_name='Our Ml Group project')


if __name__ == '__main__':
    app.run(debug=True)
