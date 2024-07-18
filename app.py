from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')


@app.route('/completed', methods=["GET","POST"])
def completed():


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)