# 🌦 Django Weather App

A modern weather forecast web application built using Django and OpenWeatherMap API.  
The application provides real-time weather information, 5-day forecasts, search history, dark mode, and animated UI.

---

## 🚀 Features

- 🔍 Search weather by city
- 🌡 Real-time temperature and humidity
- 📅 5-Day weather forecast
- 🌙 Dark mode toggle
- 🕘 Recent search history
- ❌ Delete search history
- 🎨 Modern responsive UI
- ☁ Animated weather backgrounds
- 🗄 Database integration using SQLite

---

## 🛠 Technologies Used

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- JavaScript

### Database
- SQLite

### API
- OpenWeatherMap API

---

## 📂 Project Structure

```bash
weather_project/
│
├── main/
├── static/
├── templates/
├── weather_app/
├── manage.py
└── README.md
```

---

## ⚙ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/anssshu17/weather-app-django.git
```

### 2️⃣ Move into project folder

```bash
cd weather-app-django
```

### 3️⃣ Create virtual environment

```bash
python -m venv venv
```

### 4️⃣ Activate virtual environment

#### Windows
```bash
venv\Scripts\activate
```

### 5️⃣ Install dependencies

```bash
pip install django requests
```

### 6️⃣ Run server

```bash
python manage.py runserver
```

---

## 🔑 API Setup

Get your free API key from:

https://openweathermap.org/api

Then add your API key inside:

```python
views.py
```

```python
API_KEY = "YOUR_API_KEY"
```

---

## 📸 Screenshots

(Add screenshots here later)

---

## 👨‍💻 Author

Anshu Raj

---

## ⭐ Future Improvements

- User authentication
- Weather by current location
- Deployment on cloud
- Temperature graphs
- Favorite cities
