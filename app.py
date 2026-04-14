# Flask Portfolio Web Application
# This app displays multiple pages and uses dynamic data for projects

import os
from dotenv import load_dotenv


from flask import Flask, render_template, request
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# List of projects used to dynamically generate project and skill cards on the website

projects_list = [
    {
     "title": "Manchester United Fan page", 
     "description": "A fan page dedicated to Manchester United, showcasing news, player profiles and statistics, and match updates/results in a clean, responsive design.",
     "tech": "HTML, CSS",
     "category": "Web Development"},
     
    {"title": "Game of Thrones Quiz Site", "description": "An interactive quiz site based on the popular TV series Game of Thrones, testing users' knowledge of the show's characters, plot, and trivia.",
     "tech": "HTML, CSS, JavaScript",
     "category": "Web Development"},

    {"title": "Flask Portfolio", "description": "A personal portfolio website built with Flask, showcasing projects, skills, and experience.",
     "tech": "Python, Flask, JavaScript, HTML, CSS",
     "category": "Web Development"},
]
skills_list = [
    "Python",
    "Flask",
    "HTML",
    "CSS",
    "Javascript",
    "GitHub"
]

# Flask routes are used to define the different pages of the website. Each route corresponds to a specific URL and renders a template with dynamic data passed as arguments.
# Each @app.route decorator defines the URL path for the page.
# When a user visits a URL, the corresponding function is called, which renders the appropriate HTML template and passes any necessary data to it. This allows for dynamic content to be displayed on the website based on the route accessed by the user.

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

    app.run(debug=os.getenv('DEBUG') == 'True')