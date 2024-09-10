import json

first_item = True

def initialize_json_file():
    with open('data.json', 'w') as json_file:
        json_file.write('[')  # Start the JSON array

def save_to_json(data):
    global first_item
    with open('data.json', 'a') as json_file:
        if first_item:
            json_file.write(json.dumps(data, indent=4))
            first_item = False
        else:
            json_file.write(',\n' + json.dumps(data, indent=4))


def finalize_json_file():
    with open('data.json', 'a') as json_file:
        json_file.write(']')
