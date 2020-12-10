import json

from hollymovies import models


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


def dumpdata(model, output_path):
    with open(output_path, 'w') as output_file, models.session() as session:
        _dump_model(output_file, session, model)
