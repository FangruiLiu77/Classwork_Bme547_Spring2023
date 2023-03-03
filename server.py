from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server on"


@app.route("/info", methodd=["GET"])
def info_route():
    return "This server was wrriten for BME547"


@app.route("/HDL_analysis", methods=["POST"])
def HDL_route_handler():
    """
    in_data = {"name":<patient_name>,
               "HDL_value": <HDL_result> }
    """
    from blood_calculator import HDL_analysis
    in_data = request.get_json()
    diagnosis = HDL_analysis(in_data["HDL_value"])
    return diagnosis


@app.route("/add", methods=["POST"])
def add_numbers():
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    # return jsonify(answer)
    if answer < 0:
        return "The answer was less than zero. BAD", 400
    return jsonify(answer)


@app.route("/add_two/<a>/<b>", methods=["GET"])
def add_two_handlere(a, b):
    answer = a + b
    return jsonify(answer)


if __name__ == "__main__":
    app.run()
