from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

@app.route('/story1')
def story1():
    return render_template('story1.html')

if __name__ == "__main__":
    app.run(debug=True)