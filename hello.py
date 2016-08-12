from flask import Flask, render_template
app = Flask(__name__) #python variable

@app.route('/') #decorator, falsk takes the result back into the page
def index():
    return render_template('index.html')

@app.route('/user/<name>') 
def user(name):
    return render_template('user.html', name=name) 

if __name__ == '__main__':
    app.run(debug=True)


