from flask import Flask
app = Flask(__name__) #python variable

@app.route('/') #decorator, falsk takes the result back into the page
def index():
    return "<h1> Hello, CHPT!</h1>"

if __name__ == '__main__':
    app.run(debug=True)


