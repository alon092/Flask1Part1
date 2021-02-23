# import Flask class
from flask import Flask
'''
__name__ is a special var of python that is just the name of the module.
If we run the script with python directly, then __name__ can be equal to __main__.
basically that is so flask knows where to look for ur templates and static files and things like that.
so now we have an instantiated flask applications in this app variable
'''
app = Flask(__name__)


'''
@app.route("/")
def hello():
    return "Hello World!"
'''


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello World!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)