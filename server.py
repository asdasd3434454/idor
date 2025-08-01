from flask import Flask, request

app = Flask(__name__)

# Mock database
users = {
    "22": {"name": "John", "prize": "You won!"},
    "42": {"name": "Jane", "prize": "Also a winner!"}
}

@app.route("/idor", methods=["GET"])
def idor():
    user_id = request.args.get("id")
    if user_id in users:
        return f"<h1>{users[user_id]['prize']}</h1>"
    else:
        return "<h1>Try harder!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
