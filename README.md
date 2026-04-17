# GitHub Repository
https://github.com/mdpos95-tech/flask-portfolio

# Deployed Project
https://flask-portfolio-gncf.onrender.com/

# Flask Portfolio Website

## Project description

This project is a personal portfolio website developed using Python and Flask.
The aim of the application is to showcase my web development projects, technical skills, and background in a professional format.
The website includes multiple pages, dynamic project rendering using Flask, JavaScript interactivity, and a working contact form that sends e-mails.

## Features

### Feature 1 - Dynamic Projects Page

Projects are stored in a Python list of dictionaries and rendered dynamically using Flask and Jinja templates.

### Feature 2 - Contact Form

Users can submit a contact form which sends messages directly to my e-mail using SMTP.

### Feature 3 - Dark Mode 

Users can toggle dark mode, Their preference is then saved using local storage.

### Feature 4 - Search and Filtering

Users can search projects and filter by category using JavaScript.

### Feature 5 - Responsive layout

This website is designed to work across desktop and mobile screen sizes.

----------------

## Design Choices

### Colours 

I used a modern dark/light theme with neutral colours to keep the portfolio professional and easy to read.

### Fonts / Typography

Clean sans-serif fonts were used to improve readability and create a modern user interface.

### Layout 

A clean multi-page layout with reusable navigation was chosen for consistency across pages.

### Images / Graphics

Minimal graphics were used as i wanted the focus to remain on projects and content.
I used a background-image I felt suited the theme of the site, and also created a favicon with my initials to give the website a more personal feel.

---------------

## Development Process

### Project Planning

At the beginning, I planned a portfolio website to showcase my progress in Web development with five main pages:
- Home
- Projects
- Skills
- About
- Contact

I also planned to include JavaScript interactivity and email functionality.

### Challenges Faced

One challenge was setting up the Flask contact form with Gmail SMTP authentication.
This was solved using environment variables and an app password, as Gmail blocks normal password login, so I had to research how to use an app password and store credentials securely.

Another challenge was implementing search and filtering logic with JavaScript. which was challenging as I had to make sure users could search by title, technology, and decription while also combining this with category filters.

Another challenge was finding out how to optimally get Flask templates to work with Jinja, at first, linking Python routes to HTML pages and passing data between files was confusing, but after testing render_template() and inheritance with base.html, the structure became a lot clearer.

Dark mode function was also a challenge, as I wanted the theme choice to remain after refreshing the page. This was solved using local storage.

Deploying a Flask project was more complex than deploying a static website. I had to learn how to use requirements.txt, Gunicorn, environment variables, and Render deployment settings.

Debugging errors throughout development was one of the biggesr challenges. Small mistakes such as missing brackets, incorrect indentation, route errors, or file paths often stopped the application from running, so careful testing was essential.

### Interactivity

JavaScript was used to add:

- Dark mode toggle
- Saved theme preference
- Project search
- Category filtering
- Fade-in animations
- Clickable projects cards

-------------

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Jinja
- Gunicorn
- Render

------------

## Deployed Site

This site has been deployed to GitHub Pages at the URL below:

Render URL here
