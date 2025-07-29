from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('welcome.html')

@app.route('/SkillFlip')
def skillspin():
    return render_template("skillflip.html")

@app.route('/Suggestions')
def suggestions():
    return render_template("suggestions.html")



if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0')

