from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
    return "Alô mundo! Aqui é a Tainara testando o Flask!", 200
 
app.run()
