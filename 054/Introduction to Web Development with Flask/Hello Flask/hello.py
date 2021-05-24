from flask import Flask
# import random

app = Flask(__name__)

# print(random.__name__)
# Prints name of the module of selected file (random) ==> random
# print(__name__)
# Prints name of the module of current file (hello.py) ==> __main__

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
# After running the program if go 'http://127.0.0.1:5000/' in our browser it shows 'Hello, World!' on the webpage

@app.route("/bye")
def say_bye():
    return "Bye"
# Now if we go 'http://127.0.0.1:5000/bye' it shows 'Bye' on the webpage

if __name__ == "__main__":
    app.run()               # By this we don't have to add Environment variable 'FLASK_APP', by standard run and stop keys

