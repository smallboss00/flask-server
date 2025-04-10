from flask import Flask , request

user = "salah"
password = "salah"

weapon = "pistol"

app = Flask(__name__)

@app.route("/send", methods=['POST'])
def send():
    print(request.json)
    print("todays seed is: ", request.json["seed"])
    return {"answer": None}


@app.route("/get", methods=['POST'])
def get():
    print(request.json)
    return {"answer": 1 ,"weapon" : weapon}

@app.route("/login", methods=['POST'])
def login():
    print(request.json)
    if request.json["username"] == user and request.json["password"] == password:
        return {"answer": None,'Access': 'Granted'}
    return {"answer": None ,'Access': 'Denied'}

@app.route("/")
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run()