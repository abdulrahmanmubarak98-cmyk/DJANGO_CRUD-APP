Django Crud Application

A simple yet structured CRUD (Create,Read, Update,Delete) web application built with Django.

This project was developed as part of my backend development journey to understand the core architecture of Django and how data flows through a modern web application.

The goal of this project was not only to build functionality but to deeply understand the concepts behind Django's models,views,templates, and URL routing.

# Project Overview

This application allows users to:

- Create new records
- View stored records
- Update existing records
- Delete records

The project demonstrates how a backend framework like Django manage database interaction, server logic, and dynamic HTML rendering

it also uses Bootstrap for a clean and responsive interface

# Key Features

- Full CRUD functionality
- Djnago Model-View-Template (MVT) architecture
- Template inheritance for reusable layouts
- Clean and structured URL routing
- Responsive UI with Bootstrap
- Database persistence
- Organized Django project structure

# Technologies Used

- Python
- Django
- Bootstrap
- HTML5
- CSS

# What I learned

Through building this project, i gained pratical experience with:

- Designing database models in Django
- Handling HTTP requests and response
- Implememting CRUD operations
- Using Django templates and templates inheritance
- Structuring a scalable Django project
- Integrating Bootstrap U with Django templates
- Managing migration and database updates

This project strengthened my understanding of how backend logic interacts with the frontend layer to create a dynamic web applications.

# Projecct Structure

|
|\***\*\_\_\_\*\*** manage.py
|\***\*\_\_\*\*** storefront
|\***\*\_\_\*\***settings.py
|\***\*\_\_\*\***urls.py
|\***\*\_\*\***asgi.py
|
|
|\***\*\_\*\***playground
| |***model.py
|***views.py
|***urls.py
|***admin.py
|***templates/
|
| |***base.html
| |***hello.html
| |***edit.html
| |**\_\_\_**migrations/
|
|
|
|
|
|
|
|**\_**README.md

# How To Run The Project

1. Clone the Repository
   git clone
   https://github.com/abdulrahmanmubarak98-cmyk/DJANGO_CRUD-APP.git

cd Django_Project

2. Create Virtual Environment
   python -m venv venv

Activate it:
windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate

3. Install Dependencies
   pip install -r requirement.txt

4. Apply Migrations
   python manage.py migrate

5. Run the Development Server

python manage.py runserver

Then open:
http://127.0.0.1:8000/hello/

Future Improvements

Planned enhancements for this project include:

- User authentication system (login/logout/register)
- Search and filtering functionality
- Pagination for large datasets
- Rest API integration using Django REST framework
- Form validation improvements
- Deployment to a cloud platform
- Improved UI/UX design

This improvement will help evolve this project from a learning exercise into a more production-ready backend application.

# Why This Project Matters

This project represents a key milestone in my backend development journey.

Instead of following tutorials, i focused on understanding the underlying concepts behind each layer of the application and implementing them step-by-step.

The experience gained here forms the foundation for building more advanced Django Application and scalabe backend systems.

Author
Mubarak-Adogu

Backend Developer (Python & Django)
Focused on building strong backend systems through consistency, depth of understanding, and disciplined learning.

Acknowledgment

This project is part of my continous learning journey in software engineering and backend development.

I believe consistent small improvements compound over time - a principle inspired by Atomic Habits.
