from flask import Flask, request

app = Flask(__name__)


@app.route('/<s0>')
def hello(s0):
    s1 = request.args['s1']
    return f'Hello, {s0} and {s1} world!'


if __name__ == "__main__":
    app.run()
