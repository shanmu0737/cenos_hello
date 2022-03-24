from flask import Flask,render_template,redirect

app = Flask(__name__)
app.debug = False

@app.route('/')
def index():
    return 'hello Benson'

@app.route('/hello/')
def hello():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()




























