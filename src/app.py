from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('greeting', name=username))
    return render_template('index.html')

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)