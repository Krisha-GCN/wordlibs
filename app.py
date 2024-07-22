from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def madlibs():
    if request.method == "POST":
        global adj1
        global food
        global body_part
        global spice
        global adj2
        global adj3
        global adverb
        global person
        global emoji
        global emotion
        adj1 = request.form["adj1"]
        food = request.form["food"]
        body_part = request.form["body_part"]
        spice =  request.form["spice"]
        adj2 = request.form["adj2"] 
        adj3 = request.form["adj3"]
        adverb = request.form["adverb"]
        person = request.form["person"]
        emotion = request.form["emotion"]
        return redirect('/completed', code=302)
    
    return render_template("madlibs.html")


@app.route('/completed')
def completed():
    return render_template("completed.html", 
    adj1 = adj1,
    food = food, 
    body_part = body_part,
    spice =  spice,
    adj2 = adj2, 
    adj3 = adj3,
    adverb = adverb,
    person = person, 
    emotion = emotion)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)