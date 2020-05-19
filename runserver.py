from flask import Flask
from math import sqrt

app = Flask(__name__)

@app.route('/')
@app.route('/fib')
def sequence():
    return " ".join([str(calc_num(i)) for i in range(1, 10)])

@app.route('/fib/<int:position>')
def position(position):
    return str(calc_num(position))

def calc_num(n):
    val = int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
    return val

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
