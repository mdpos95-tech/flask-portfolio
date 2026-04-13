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

@app.route("/projects")
def projects():
    return render_template('projects.html', title='Projects', projects=projects_list)

@app.route("/skills")
def skills():
    return render_template('skills.html', title='Skills', skills=skills_list)
@app.route("/about")
def about():
    return render_template('about.html', title='About')
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    message = ""
    if request.method == 'POST':
        name = request.form.get('name')
        message = f"Thanks, {name}! Your message has been received."
        
        return render_template('contact.html', title='Contact', message=message)


if __name__ == '__main__':

    app.run(debug=True)