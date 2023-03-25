import json

def get_data_operation(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)
