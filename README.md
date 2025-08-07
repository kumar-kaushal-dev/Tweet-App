# 🐦 TweetApp — A Mini Twitter Clone Built with Django

> **TweetApp** is a feature-rich Django web application that mimics core Twitter functionality. Users can create, edit, and delete tweets — including images — all wrapped in a responsive UI built with Bootstrap.

---

## 🚀 Features

- 🧾 **User-friendly tweet creation & editing**
- 🖼️ **Image upload support**
- 🎨 **Fully responsive design using Bootstrap**
- 🔐 **Environment variable handling with `python-decouple`**
- 🗃️ **Media management (images stored and served locally)**
- ⚙️ **Clean MVC architecture with Django best practices**
- 📑 **Custom styling through static files (CSS)**

---

## 🧰 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap 5
- **Backend:** Django (Python)
- **Database:** SQLite3 (default for local development)
- **Other Tools:** python-decouple, Pillow

---

---

## 🔧 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Tweet-App.git
   cd Tweet-App

---
2. **Create a Virtual Environment**

python -m venv venv
venv\Scripts\activate  # for Windows

---
3. **Install Requirements**

pip install -r requirements.txt

---
4. **Set Up .env Create a .env file in the root folder:**

DEBUG=True
SECRET_KEY=your_django_secret_key

---
5. **Run Migrations**

python manage.py migrate

---
6. **Run the Development Server**

python manage.py runserver

---

7. **Run the Development Server**

python manage.py runserver

---


📁 Project Structure

tweetproject/
│
├── media/                  # Uploaded images
├── static/css/style.css    # Custom styling
├── templates/              # HTML templates
├── tweet/                  # Main Django app (views, models)
├── tweetproject/           # Project settings and URLs
├── db.sqlite3              # Local DB (ignored in Git)
├── manage.py
├── requirements.txt
└── .gitignore

---

🙋 About Me
Kaushal Kumar
-💼 Full Stack Developer | Cloud Enthusiast | Freelancer

---

💡 Future Improvements
-User authentication system

-Like/comment feature

-Pagination for tweets

-Deployment on Heroku or Vercel (with PostgreSQL)
