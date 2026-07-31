from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the App"

@app.route("/health")
def health():
    return "App is running"

# Dictionary to store votes
votes = {}

# Vote for a candidate
@app.route("/vote/<name>")
def vote(name):
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

    return f"Vote recorded for {name}. Total votes: {votes[name]}"

@app.route("/reset")
def reset():
    votes.clear()  # Remove all votes
    return "All vote counts have been reset."

# Show results
@app.route("/results")
def results():
    return jsonify(votes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)