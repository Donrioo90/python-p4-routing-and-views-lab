#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1. Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2. Print string route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

# 3. Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(i) for i in range(parameter)]
    return "<br>".join(numbers)

# 4. Math operations route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
