

---

# 🌾 FarmCare - Django Project Setup Guide for Beginners

Welcome to **FarmCare**! This guide will walk you through setting up a Django project from scratch with step-by-step instructions and helpful explanations for beginners.

---

## 📁 Project Initialization

### 1. Create Your Project Folder
```bash
# Create a folder for your project
mkdir farmcare
cd farmcare
```

---

## 🛠 Installing Django

```bash
pip install Django
```

### ✅ Verify Installation
```bash
python
>>> import django
>>> django.__version__
# You'll see the version if Django is installed correctly
# Press Ctrl + Z (Windows) to exit Python shell
```

---

## 🚀 Starting a Django Project

```bash
django-admin startproject farmcare
cd farmcare
```

---

## 🧪 Create a Virtual Environment (optional but recommended)

### 1. Install virtualenv
```bash
pip install virtualenv
```

### 2. Create Virtual Environment
```bash
virtualenv env
```

### 3. Activate Environment (Use CMD not PowerShell!)
```bash
cd env/Scripts
activate
```

🟢 Your command line will now look like this:
```
(env) C:\Users\ADITI KIRAN MAHABOLE\Desktop\farmcare\farmcare\env\Scripts>
```

### 4. Navigate back to the `farmcare` folder
```bash
cd ../..
```

### 5. Re-install Django inside the virtual environment
```bash
pip install django
```

---

## 📦 Create a Django App

You can create multiple apps like `buysell`, `accounts`, or `home`.

```bash
python manage.py startapp buysell
```

---

## 🧩 Run Migrations & Start Server

```bash
python manage.py migrate
python manage.py runserver
```

🌐 Open the link displayed in your terminal in a browser to see your app running.

### Optional: Use Custom Port
```bash
python manage.py runserver 0.0.0.0:5000
```

---

## ⚙️ Add App to Installed Apps

Edit `farmcare/settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'buysell',
]
```

---

## 🧠 Understanding Django Basics

| Concept       | File                  | Purpose                                       |
|---------------|-----------------------|-----------------------------------------------|
| Views         | `views.py`            | Logic and response handling                   |
| Routing       | `urls.py`             | URLs and routing configuration                |
| Database/Tables | `models.py`          | Defining schema with Django models            |
| Templates     | `templates/` folder   | HTML files to render UI                       |
| Static Files  | `static/` folder      | CSS, JS, images, etc.                         |

---

## 📥 Installing Dependencies

Run these commands **inside your activated virtual environment** (or outside if needed):

```bash
pip install joblib
pip install scikit-learn
pip install requests
pip install numpy 
pip install pandas
pip install tensorflow
pip install pymysql
```

### ⚠️ TensorFlow Note:
If installation fails inside the virtual environment, deactivate it and run the above commands globally.

---

## 🛠 pymysql Setup

To use MySQL with Django, add the following inside both:

- `farmcare/__init__.py`
- `buysell/__init__.py`

```python
import pymysql
pymysql.install_as_MySQLdb()
```

---

## 🧱 Working with Models

### Example: Create Models in `buysell/models.py`

```python
from django.db import models

class FormModel(models.Model):
    name = models.CharField(max_length=100)

class MandiDetails(models.Model):
    location = models.CharField(max_length=200)
```

### Save & Apply Changes

```bash
python manage.py makemigrations
python manage.py migrate
```

> 🔁 Run these every time you update your models.

---

## 🖼️ Using Static Files

### Folder Structure
- Create a folder: `buysell/static/`
- Place your CSS, JS, or images inside it

### Update `settings.py`

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'buysell/static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'buysell/assets')
```

### Collect Static Files

```bash
python manage.py collectstatic
```

📁 This command creates the `assets/` folder that Django uses internally.

### In Your HTML Templates

At the top of each HTML file, add:

```django
{% load static %}
```

Then use your static files like:

```html
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

---

## 🔍 Bonus: Search Implementation Using `__icontains`

You can perform case-insensitive searches in Django queries like:

```python
FormModel.objects.filter(name__icontains="query")
```

Useful for building search bars or filters.

---

## 💡 Tips

- Always activate the virtual environment before installing dependencies.
- Don’t forget to include apps in `INSTALLED_APPS`.
- Run `makemigrations` and `migrate` after any model changes.
- Use `__icontains` for search functionality.
- Don’t forget `{% load static %}` in HTML templates when using CSS or images.

---

## ✨ Happy Coding!

Let me know if you'd like me to turn this into a downloadable `README.md` file!
