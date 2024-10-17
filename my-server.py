# curl -d "text=Hello Rislyn&param2=value2" -X POST http://localhost:5000/echo

# curl -d "text=Hello Rislyn&param2=value2" -X POST "https://supreme-space-palm-tree-5g46pvpjgxpj27wx7-5000.app.github.dev/echo"

from flask import Flask, request

app = Flask(__name__)

authData = {
    "id": "rislyn_ferona.raja@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

@app.route("/")
def hello():
    return " you called \n"

@app.route("/echo", methods=['POST'])
def echo():
    return "You said: " + request.form['text']

@app.route("/auth", methods=['POST'])
def login():
    print(request.form)
    if request.form['id'] in authData["id"]:
        if request.form['token'] == authData['token']:
            return "Yes a match"
        else:
            return "No match"
    return "Nothing"

if __name__ == "__main__":
    app.run(host='0.0.0.0')