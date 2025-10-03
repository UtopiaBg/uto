from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/huts')
def huts():
    return render_template('huts.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')

if __name__ == '__main__':
    app.run(debug=True)
