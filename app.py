# Flask Portfolio Web Application
# This app displays multiple pages and uses dynamic data for projects

import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


from flask import Flask, render_template, request

# Load environment variables from .env file for sensitive information like email credentials and secret keys.
# Keeps passwords and keys out of the codebase for better security and allows for easy configuration across different environments.

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Email settings used by contact form SMTP system for security reasons.

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')

# List of projects used to dynamically generate project and skill cards on the website

projects_list = [
    {
     "title": "Manchester United Fan page", 
     "description": "A fan page dedicated to Manchester United, showcasing news, player profiles and statistics, and match updates/results in a clean, responsive design.",
     "tech": "HTML, CSS",
     "category": "Web Development",
     "live": "https://mdpos95-tech.github.io/",
     "github": "https://github.com/mdpos95-tech/mdpos95-tech.github.io"},
     
    {"title": "Game of Thrones Quiz Site", "description": "An interactive quiz site based on the popular TV series Game of Thrones, testing users' knowledge of the show's characters, plot, and trivia.",
     "tech": "HTML, CSS, JavaScript",
     "category": "Web Development",
     "live": "https://mdpos95-tech.github.io/javascript-lab/",
     "github": "https://github.com/mdpos95-tech/javascript-lab"},

    {"title": "Flask Portfolio", "description": "A personal portfolio website built with Flask, showcasing projects, skills, and experience.",
     "tech": "Python, Flask, JavaScript, HTML, CSS",
     "category": "Web Development",
     "live": "https://flask-portfolio-gncf.onrender.com/",
     "github": "https://github.com/mdpos95-tech/flask-portfolio"
     },
]

# List of skills used to dynamically generate skill cards on the website.

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

# Contact page handles form display and message sending.

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    message = ""

#Process submitted contact form data.

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        user_message = request.form.get('message')

#Built email message using visitor form input.

        try:
            msg = EmailMessage()
            msg['Subject'] = f'Portfolio Contact Form Message from {name}'
            msg['From'] = EMAIL_USER
            msg['To'] = EMAIL_RECEIVER
            msg['Reply-To'] = email 

            msg.set_content(
                f"Name: {name}\n"
                f"Email: {email}\n\n"
                f"Message:\n{user_message}"
            )

# Securely connect to Gmail SMTP server and send message using credentials stored in environment variables.

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(EMAIL_USER, EMAIL_PASS)
                smtp.send_message(msg)

            # Create the email message
            message = f"Thanks, {name}! Your message has been received."
        except Exception as e:
            message = "An error occurred while sending the message. Please try again."
        
    return render_template('contact.html', title='Contact', message=message)


if __name__ == '__main__':

    # Debug mode is controlled using environment variables for better security.

    app.run(debug=os.getenv('DEBUG') == 'True')