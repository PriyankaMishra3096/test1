from flask import Flask, request, jsonify
import sys

app = Flask(__name__)


def add(a, b):
    res = a + b
    return str(res)


@app.route("/", methods=['GET'])
def demo():
    msg = "Hello There!"
    return msg


@app.route("/gcp_demo", methods=['GET', 'POST'])
def create_gcp_demo():
    req_data = request.get_json()
    a = 0
    b = 1
    if request.method == 'POST':
        print("req_data>>>>>>>>>>>>>>>>>>>> ", req_data)
        a = req_data.get("first_arg")
        b = req_data.get("second_arg")
    sum = add(a, b)
    result = {"Sum": sum}
    return jsonify(result)


@app.route("/gcp_demo_2", methods=["GET"])
def create_gcp_demo2():
    a = 10
    b = 20
    sum = add(a, b)
    result = {"Sum": sum}
    return jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
