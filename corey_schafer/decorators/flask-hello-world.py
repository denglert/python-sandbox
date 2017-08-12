#!/usr/bin/env python
# - This is an example use-case for decorators with arguments.
# - flask library
# - `app.route` decorator accepts arguments.


from flask import Flask
app = Flask(__name__)


# - The argument is the URL path, here the root, /
@app.route("/")
def hello():
    return "Hello world!"

# - The argument is the URL path, here /about
@app.route("/about")
def about():
    return "About page"

if __name__ == "__main__":
    app.run()
