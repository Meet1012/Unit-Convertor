# 🌐 Django Unit Converter Web App

[![Django](https://img.shields.io/badge/Django-4.0%2B-brightgreen)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)


A versatile **Unit Converter** web application built with the **Django** framework. This web app allows users to convert between units of **Length**, **Weight**, and **Temperature** with a user-friendly interface.!['Project Link'](https://roadmap.sh/projects/unit-converter)

## 📋 Features

- 🔄 **Length Conversion**: Convert between meters, kilometers, miles, and more.
- ⚖️ **Weight Conversion**: Convert between kilograms, pounds, grams, etc.
- 🌡️ **Temperature Conversion**: Convert between Celsius, Fahrenheit, and Kelvin.
- 🧑‍💻 **Responsive UI**: Mobile-friendly, clean, and modern design using HTML, CSS, and JavaScript.
- 🌍 **Flexible Navigation**: Switch between conversion types via tabs without page reloads.
- 🚀 **Real-time Conversions**: Submissions processed without reloading the entire page using Django forms and logic.

## 📷 Screenshots

![Unit Converter](https://assets.roadmap.sh/guest/unit-converter-be-project.png)  <!-- Replace this with an actual screenshot URL -->

## 🛠️ Tech Stack

- **Django**: Backend framework for the web app.
- **Python**: The core language for logic and unit conversions.
- **HTML/CSS/JavaScript**: For building the frontend interface.
- **Bootstrap/TailwindCSS**: (Optional) Frameworks to improve the UI design.

## 🚀 Getting Started

Before running the project, ensure you have the following installed: **Python 3.8+** and **Django 4.0+**. 

### Installation Steps

1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/unit-converter-django.git
   cd unit-converter-django

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt

3. Run Migrations: Set up the database by applying migrations:
    ```bash
    python manage.py migrate

4. Start the Development Server: Launch the server to view the application locally:
    ```bash
    python manage.py runserver

5. Access the Application: Open your web browser and navigate to:
    ```bash
    http://127.0.0.1:8000/
    
## 📄 Usage

1. **Select Conversion Type**: Choose from Length, Weight, or Temperature by clicking the respective tab.
2. **Input Values**: Enter the value you want to convert and select the unit you are converting from and to.
3. **Convert**: Click the "Convert" button, and the result will be displayed immediately without a page refresh.

## 🔧 Customization

Feel free to customize the conversion logic in `views.py` to add more units or modify existing ones. You can also tweak the UI components by editing the HTML files located in the `static` directory.


Happy converting! 🚀
