Django CRUD & Authentication App

# Overview

This project is a full-stack Django application thatimplement a secure authentication system and a robust CRUD(Create, Read, Update, Delete) functionality. It demonstrates core Django concepts including models, views, templates,form, user authentication and relational database management.

This app was built as part of my journey to master Django, Python web development, and full-stack application design.

# Features

Authentication

- User Registration (Sign Up) with validation
- Login & Logout functionalitie
- Password Hashing for secure credential storage
- Access Control: Only authebticated users can access certain views.

CRUD Operations

- Create new records
- Read and view detailed records
- Update existing records with form validation
- Delete records
- Dynamic Template Rendering using Django's templating engine

Database

- Built with Django ORM and SQLite by default
- Relationship handled with foreign Keys and QuerySet filtering for efficient data management

# Tech Stack

- Backend: Python, Django
- Frontend: HTML5, CSS3, Bootstrap (optional for styling)
- Database: SQLite(default), Django ORM
- Version Control: Git & GitHub

#Projecct Structure
| |**\_\_\_** manage.py |**\_\_** storefront |\***\*\_\_**settings.py |**\_\_**urls.py |**\_**asgi.py | | |**\_\*\***playground | |***model.py |***views.py |***urls.py |***admin.py |***templates/ | | |***base.html | |***hello.html | |*edit.html | signup.html |*\_\_migrations/ | | | | | | | |***README.md

# Installation

1. Clone the repository
   git clone
   https://github.com/abdulrahmanmubarak98-cmyk/DJANGO_CRUD-APP.git
2. Create a virtual environment
   python -m venv venv

   Linux/MacOs
   source env/bin/activate

   windows
   venv/Scripts/activate

3. Install dependeecies

   pip install -r requirement.txt

4. Apply migration

   python manage.py makemigrations
   python manage.py migrate

5. Run the development server

   python manage.py runserver

   visit http://127.0.0.1:8000/ in your browser

# Usage

1. Sign Up: Create a new user account
2. Login: Access the dashboard and manage records
3. Create/Read/Update/Delete: Manage data entries seamlessly
4. Logout: Securely end your session

# Future Improvement

- Implement role-based acess control (Admin vs User privileges)
- Add AJAX-powered forms for smoother CRUD operations
- Integrate REST API endpoints for external applications
- Enhance UI/UX with modern frameworks like React or Tailwind CSS

# Learning & Takeaways

- Strengthened understanding of Django models, views, and template
- Learned how to implement secure authentication & password hashing
- Gained experience with relational databases and query optimization
- Built a full-stack project that combines backend logic with user-friendly frontend template

# Contact & Collaboration

- GitHub: https://github.com/abdulrahmanmubarak98-cmyk
- LinkedIn: https://www.linkedin.com/in/mubarak-adogu-abdulrahman-adogu1
