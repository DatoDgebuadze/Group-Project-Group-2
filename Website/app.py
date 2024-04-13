from flask import Flask, render_template
from markupsafe import escape
# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its corresponding function


#--- Routes------------

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
# 
# def index(name=None):
#     print(f"Rendering index.html with name: {name}")  # Debugging line
#     return render_template('Templates/index.html', name=name)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
