from flask import Flask
app = Flask("calculator")

@app.route("/")
def index():
    return "Addition: /add/Number1/Number2 Substraction: /sub/Number1/Number2 Multiplication: /mul/Number1/Number2 Division: /div/Number1/Number2"

@app.route("/add/<float:number_1>/<float:number_2>")
def plus(number_1, number_2):
    number_3 = number_1 + number_2
    return "{}".format(number_3)

@app.route("/sub/<float:number_1>/<float:number_2>")
def minus(number_1, number_2):
    number_3 = number_1 - number_2
    return "{}".format(number_3)

@app.route("/mul/<float:number_1>/<float:number_2>")
def mult(number_1, number_2):
    number_3 = number_1 * number_2
    return "{}".format(number_3)
    
@app.route("/div/<float:number_1>/<float:number_2>")
def div(number_1, number_2):
    if number_2 == 0:
        return "NaN"
    else:
        number_3 = number_1 / number_2
        return "{}".format(number_3)