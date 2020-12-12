from flask import Blueprint, render_template, request

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/<s0>')
def hello(s0):
    s1 = request.args['s1']
    return render_template(
        'hello.html', adjectives=[s0, s1, 'beautiful', 'wonderful']
    )
