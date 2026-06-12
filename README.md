
# 🛒 Django Shop — Dadisiweb Demo App

This project is a **mini eCommerce / CRUD platform** built to demonstrate how Django applications can be deployed, hosted, and managed using **Dadisiweb Cloud**.

It includes:

* Product catalog (CRUD)
* Shopping cart logic
* Admin dashboard
* PostgreSQL integration
* Minimal Django templates
* Production-ready WSGI deployment (Gunicorn)

---

# 🧠 What This Demonstrates

* Full-stack Django application structure
* Database-driven backend (PostgreSQL)
* Admin-powered content management
* Server deployment with Gunicorn
* Cloud-ready architecture via Dadisiweb

---

# 🚀 Getting Started (Deploy on Dadisiweb)

Follow these steps to deploy your own version:

---

## 1. 🍴 Fork the Repository

Fork this repository to your GitHub account.

---

## 2. 🧑‍💻 Create a Dadisiweb Account

Go to:

👉 [https://dashboard.dadisiweb.com](https://dashboard.dadisiweb.com)

Create your account and log in.

---

## 3. 📥 Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/deploy-django-shop.git
cd deploy-django-shop
```

---

## 4. 📦 Install Dependencies

```bash
pip install django psycopg2-binary pillow django-environ gunicorn
```

---

## 5. 🗄️ Database & Settings

All database configuration is handled inside `settings.py`.

Ensure PostgreSQL connection is correctly configured before deployment.

---

## 6. 🚀 Production Run (Dadisiweb / Server)

Use Gunicorn:

```bash
gunicorn deploy_django_shop.wsgi:application --bind 0.0.0.0:8001
```

---

# 🌐 Deploy on Dadisiweb

* Go to Dadisiweb Dashboard
* Create a **New Project**
* Select **Django App / Custom App**
* Connect your GitHub repo

---

# ⚙️ Build Settings (Dadisiweb)

### Build Command

```bash
pip install -r requirements.txt && python manage.py migrate
```

### Run Command

```bash
gunicorn deploy_django_shop.wsgi:application --bind 0.0.0.0:8001
```

---

# 🧠 Project Features

* 🛍 Product listing system
* 🧾 CRUD product management
* 🛒 Shopping cart logic
* 🧑‍💼 Django admin panel
* 🗄 PostgreSQL persistence
* 🚀 WSGI production deployment

---

# ⚡ Notes

* This is a demo eCommerce system (not production billing-ready)
* Designed for showcasing Django deployment on Dadisiweb
* All environment and DB configuration is handled in `settings.py`

---

# 🌍 Powered By

**Dadisiweb Cloud**
Deploy. Scale. Control.
# django-shop
