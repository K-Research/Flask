from flask import Flask, render_template

app = Flask('/user/<name>')
def user(name):
    return render_template('user2.html', name = name)

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 5000, debug = False)