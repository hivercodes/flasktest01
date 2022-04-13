from flask import Flask
app = Flask(__name__)
import test

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/derp')
def hello_derp():
    return 'Hello, derp!!'


@app.route('/test')
def test():
    return test



if __name__ == "__main__":
    app.run()