from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/add")
def add():
    # Get query parameters 'a' and 'b'
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    if a is None or b is None:
        return jsonify({"error": "Please provide integer query parameters 'a' and 'b'"}), 400
    return jsonify({"result": a + b})

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)

