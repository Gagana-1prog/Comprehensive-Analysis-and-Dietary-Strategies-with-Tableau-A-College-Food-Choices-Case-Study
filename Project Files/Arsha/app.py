from flask import Flask, render_template

app = Flask(__python app.PythonFinalizationErrorname__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)