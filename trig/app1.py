from flask import Flask, request
import math

app = Flask("hello")

@app.route("/")
def index():
    return "You expected this to say hello, but it says \"donkey swings\" instead. Who would have guessed?"

@app.route("/trig/<func>")
def trig(func):
    try:
        if func == "sin":
            angle = float(request.args["angle"])
            sin = math.sin(angle)
            return "{}".format(sin)
        if func == "cos":
            angle = float(request.args["angle"])
            cos = math.cos(angle)
            return "{}".format(cos)
        if func == "tan":
            angle = float(request.args["angle"])
            tan = math.tan(angle)
            return "{}".format(tan)
    except KeyError:
        return "Missing query parameter: name", 400