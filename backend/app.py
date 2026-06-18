from flask import Flask, render_template

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John", "department": "DevOps"},
    {"id": 2, "name": "Alice", "department": "Developer"},
    {"id": 3, "name": "David", "department": "QA"}
]

@app.route("/")
def home():
    return render_template("employees.html", employees=employees)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
