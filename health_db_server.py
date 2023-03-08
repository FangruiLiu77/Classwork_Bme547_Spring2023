"""
Database = Dictionary
keys -> ids for the patients
value: int

{1: {"id": 1, "name": "David", "blood_type": "o+" },
 2: {"id": 1, "name": "David", "blood_type": "o+"},
 3: {"id": 1, "name": "David",
    "blood_type": "o+", "tests": []}
 }
"""
from flask import Flask, request, jsonify

db = {}

app = Flask(__name__)

def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id,
                   "name": name,
                   "blood_type": blood_type,
                   "test": []}
    db[id] = new_patient
    print(db)


def add_test_to_db(id, test_name, test_result):
    db[id]["test"] =  {"id": id,
                       "test_name:": test_name,
                       "test_result": test_result}

@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # Get input data
    in_data =  request.get_json()
    answer, status_code = new_patient_driver(in_data)
    return jsonify(answer), status_code
# call other functions to do the work
# return a respons


def new_patient_driver(in_data):
    # Validate input
    validation = validate_input_data(in_data)
    if validate_input_data is not True:
        return validation, 400
    # Do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # Return an answer
    return "Patient successfully added", 200


def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expect_keys = ["name", "id", "blood_type"]
    expect_types = [str, int, str]
    for key, value_type in zip(expect_keys, expect_types):
        if key not in in_data:
            return f"Key {key} is missing from the Input"
        if type(in_data[key]) is not value_type:
            return  f"Key {key} has the incorrect value type"
        return True
    
@app.route("/add_test", methods=["POST"])
def test_new_patient():
    # Get input data
    in_data =  request.get_json()
    answer, status_code = new_patient_driver(in_data)
    return jsonify(answer), status_code
# call other functions to do the work
# return a respons


def does_patient_exit_in_db(id):
    if id in db:
        return True
    else:
        return False


def test_data_driver(test_data):
    # Validate input
    validation = validate_test_data(test_data)
    if validate_test_data is not True:
        return validation, 400
    # Do the work
    add_test_to_db(test_data["id"],
                      test_data["test_name"],
                      test_data["test_result"])
    # Return an answer
    return "Test data successfully added", 200

def validate_test_data(test_data):
    if type(test_data) is not dict:
        return "Test data is not a dictionary"
    expect_keys = ["id", "test_name", "test_result"]
    expect_types = [int, str, int]
    for key, value_type in zip(expect_keys, expect_types):
        if key not in test_data:
            return f"Key {key} is missing from the test_data"
        if type(test_data[key]) is not value_type:
            return  f"Key {key} has the incorrect value type"
        return True
    

if __name__ == "__main__":
    app.run()

