from flask import Flask, render_template, request

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        messages.append({'username': username, 'message': message})
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run()
