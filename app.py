from flask import Flask, render_template, request
app = Flask(__name__)
projects_list = [
    "Project 1: Football Team Fan Site",
    "Project 2: Game of Thrones Quiz Site",
    "Project 3: Flask Portfolio"
]
skills_list = [
    "Python",
    "Flask",
    "HTML",
    "CSS",
    "Javascript",
    "GitHub"
]

@app.route('/')
def home():
    return render_template('index.html', title='Home')

if __name__ == '__main__':

    app.run(debug=True)