from flask import Flask, request, jsonify
from google.cloud import bigquery
import os

app = Flask(__name__)
client = bigquery.Client()

# Replace with your BigQuery dataset and table name
dataset_name = 'ds_company'
table_name = 'tbl_persona'

@app.route('/person', methods=['POST'])
def add_person():
    content = request.json
    doc_identidad = content['doc_identidad']
    nombre = content['nombre']
    apellido = content['apellido']

    table_id = f"{client.project}.{dataset_name}.{table_name}"

    rows_to_insert = [
        {u"doc_identidad": doc_identidad, u"nombre": nombre, u"apellido": apellido}
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False, "errors": errors}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))