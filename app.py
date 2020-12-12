from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<s0>')
def hello(s0):
    s1 = request.args['s1']
    return render_template(
        'hello.html', adjectives=[s0, s1, 'beautiful', 'wonderful']
    )


if __name__ == "__main__":
    app.run()
