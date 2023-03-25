import json


def load_file_data(filename):
    """Loads JSON data from file."""

    fh = open(filename)
    json_str = fh.read()
    notes = json.loads(json_str)
    fh.close()
    return notes


def save_data_to_file(filename, books):
    """Saves the notes to file as JSON."""

    notes_json = json.dumps(books, indent=4)
    fh = open(filename, "w")
    fh.write(notes_json)
    fh.close()
