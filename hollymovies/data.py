import json

from hollymovies import models
from hollymovies.models import all_models


def _to_dict(columns, entry):
    return {column: getattr(entry, column) for column in columns}


def _dump_entry(table, entry):
    columns = [column.name for column in table.columns]
    fields = _to_dict(columns, entry)
    return json.dumps({'model': table.name, 'fields': fields})


def _dump_model(output_file, session, model):
    for entry in session.query(model):
        dumped_query = _dump_entry(model.__table__, entry)
        output_file.write(f'{dumped_query}\n')


def dumpdata(output_path):
    with open(output_path, 'w') as output_file, models.session() as session:
        for model in all_models():
            _dump_model(output_file, session, model)


def _objects_to_add(table_to_model, input_file):
    for line in input_file:
        entry = json.loads(line)
        model = table_to_model[entry['model']]
        yield model(**entry['fields'])


def loaddata(input_path):
    with open(input_path) as input_file, models.session() as session:
        table_to_model = {model.__tablename__: model for model in all_models()}
        objects = _objects_to_add(table_to_model, input_file)
        session.bulk_save_objects(objects)
