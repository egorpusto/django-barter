# Barter Exchange Platform (Django)

A simple web platform where users can post items and make exchange offers with other users. Built with Django, focused on clarity and functionality.

## ✨ Features

- User authentication via Django's built-in system
- Create, edit, and delete item listings
- Upload images by URL
- Search and filter listings by category and condition
- Make exchange proposals between items
- Accept or decline incoming proposals
- Clean and beginner-friendly HTML interface (no API)

## 🛠 Technologies

- Django
- Python
- SQLite
- HTML

## 🚀 Getting Started

### 1. Clone the project

git clone https://github.com/egorpusto/django-barter.git
cd django-barter

### 2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run migrations

python manage.py migrate

### 5. Create a superuser (for admin panel)

python manage.py createsuperuser

### 6. Start the development server

python manage.py runserver

Visit:

- http://127.0.0.1:8000/ — main interface
- http://127.0.0.1:8000/admin/ — admin panel

## ✅ Testing

Run unit tests:

python manage.py test

## 🗂 Project Structure

* ads/ — the main app for listings and exchange proposals
* ads/templates/ads/ — HTML templates
* ads/forms.py — Django forms for ads and proposals
* ads/views.py — views and logic
* ads/urls.py — routes
* README.md — you're reading it!

## 👨‍💻 For Recruiters

This project was built as a technical assignment to demonstrate the ability to:

- Work with Django's ORM, templates, and views
- Create simple, clean interfaces
- Implement user permissions and access control
- Structure code for maintainability

Feel free to explore the code or contact me for more info!

---

Made with ❤️ by egorpusto