Django CRUD Application with Authentication & Authorization

A full-featured Django web application that implements CRUD(Create, Read, Update, Delete)
operations alongside a secure Authentication & Authorization sysytem. This project demonstrates best practices for building scalabe, secure, and production-ready backend systems using Django.

# Features

Authentication System

- User Registration (Sign Up)
- Secure Login & Logout
- Password Hashing using Django's built-in authentication system
- Session-based authentication

Authorization

- Restricted access to authenticated users only
- User-specific data handling
- Permission-based control(basic-level)

CRUD Functionality

- Create new records
- Read/view records
- Update existing records
- Delete records with confirmation

UI Structure

- Base template for consistent layout(base.html)
- Reusable template structure
- Clean and minimal interface (ready for UI upgrade)

# Tech Stack

- Backend: Django (Python)
- Frontend: HTML,CSS,(Django Templates)
- Database: SQlite(default,easily configurable to POSTgreSQL)

# Projecct Structure

| |**\_\_\_** manage.py |**\_\_** storefront |\***\*\_\_**settings.py |**\_\_**urls.py |**\_**asgi.py | | |**\_\*\***playground | |***model.py |***views.py |***urls.py |***admin.py |***templates/ | | |***base.html | |*\*\*hello.html | |*edit.html | signup.html ||login.html\*\_\_migrations/ | manage.py|db.sqlite3 | | | | | |

# Installation & Setup

1. Clone the Repository
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

   python manage.py migrate

5. Run the development server

   python manage.py runserver

   visit http://127.0.0.1:8000/ in your browser

# Key Learning Highlights

- Implemented Django authentication system from scratch
- Understood how sessions and password hashing work
- Built complete CRUD functionality using Django views and templates
- Structured reusable templates for scalability
- Applied access control using login restricitons

# Future Improvement

- Deployment with Render
- Advanced permission system(role-based access)
- REST API integration(DJANGO REST framework)
- UI/UX upgrade (Bootstrap/Tailwind)
- Email verification system
- Password reset functionality

# Contribution

Contribution,issues,and features requests are welcome

# AUTHOR

Mubarak-Adogu
Python Developer | Django Backend Developer | Automation Enthusiast

"Perseverance through bugs is what a developer from average to exceptional"
