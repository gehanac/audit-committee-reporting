from flask import Flask, request
from middleware.sanitize import sanitize_input

# Step 1: Create Flask app
app = Flask(__name__)

# ✅ Step 2: Register middleware HERE
app.before_request(sanitize_input)

# Step 3: Define routes
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    return {"response": f"You said: {user_message}"}

# Step 4: Run app
if __name__ == "__main__":
    app.run(debug=True)