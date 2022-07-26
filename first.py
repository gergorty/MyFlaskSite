from flask import Flask, redirect, url_for, render_template
import os

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html", content="Testing")



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)
