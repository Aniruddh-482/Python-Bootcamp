from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return 'Hello, World!'
# Rendering HTML and CSS Elements with Flask
@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'


# @app.route("/bye")
# def say_bye():
#     return "Bye"
# Challenge: Use Python Decorators to Style HTML Tags
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"


# How to extract the parts that we want from a URL by using variable paths

# @app.route("/username/<name>")             # Taking input in variable 'name' after '/username/' in the URL
# @app.route("/<name>")                      # Taking input in variable 'name' in the URL
# @app.route("/username/<name>/1")           # Taking input in variable 'name' after '/username/' and also '/1' in the end of the URL
# @app.route("/username/<path:name>")        # Now it takes hole path we entered after '/username/' in the URL
# def greet(name):
#     return f"Hello {name}!"

@app.route("/username/<name>/<int:number>")  # Now it takes string input in variable 'name' and int input in variable 'number' in the URL
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)              # To on the debugger (it activates the automatic reloader, whenever we make any changes)
                                     # Also it enables the debug mode on the Flask application.
