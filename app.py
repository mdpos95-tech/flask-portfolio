# Flask Portfolio Web Application
# This app displays multiple pages and uses dynamic data for projects

from email.mime import message

from flask import Flask, render_template, request
app = Flask(__name__)

# List of projects used to dynamically generate project and skill cards on the website

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

    app.run(debug=True)