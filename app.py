from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/welcome')
def contact():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
