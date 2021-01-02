from os import environ as E

import click
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

from hollymovies.data import dumpdata, loaddata
from hollymovies.models import db
from hollymovies.views import main_blueprint

DB_CONFIG = {
    key: E[f'DB{key}'] for key in ['SCHEMA', 'USER', 'PASS', 'HOST', 'PORT']
}
DB_URI_TEMPLATE = '{SCHEMA}://{USER}:{PASS}@{HOST}:{PORT}'

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI_TEMPLATE.format(**DB_CONFIG)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Fnioz1Cnl2grWSA2MLEbCrBuJjJK0ELB'
db.init_app(app)
Migrate(app, db)
Bootstrap(app)


_DUMPDATA_HELP = (
    'Dumps data from the database as json lines to provided file path.'
)


@app.cli.command('dumpdata', help=_DUMPDATA_HELP)
@click.option('--output-file', type=click.File('w'), help='Output file name.')
def dumpdata_command(output_file):
    dumpdata(output_file)


_LOADDATA_HELP = 'Loads data from provided json-lines file to the database.'


@app.cli.command('loaddata', help=_LOADDATA_HELP)
@click.option('--input-file', type=click.File('r'), help='Input file name.')
def loaddata_command(input_file):
    loaddata(input_file)


if __name__ == "__main__":
    app.run()
