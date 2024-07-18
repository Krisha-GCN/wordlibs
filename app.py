from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')


@app.route('/completed', methods=["GET","POST"])
def completed():
    if request.method == "POST":
        return render_template("completed.html", 
            adj1 = request.form["adj1"],
            food = request.form["food"], 
            body_part = request.form["body_part"],
            spice =  request.form["spice"],
            adj2 = request.form["adj2"], 
            adj3 = request.form["adj3"],
            adverb = request.form["adverb"],
            person = request.form["person"], 
            emotion = request.form["emotion"])

    return render_template("madlibs.html", url=url_for("madlibs"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)