from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage (login page)
@app.route("/")
def login():
    return render_template("login.html")

# Route for the main page
@app.route("/main")
def main():
    return render_template("main.html")

# Route to handle comment submission
@app.route("/submit_comment", methods=["POST"])
def submit_comment():
    comment = request.form.get('comment')
    username = request.form.get('username')  # You could save this to a database
    # For now, we simply print the comment and username
    print(f"Comment from {username}: {comment}")
    return "Comment submitted!"

if __name__ == "__main__":
    app.run(debug=True)