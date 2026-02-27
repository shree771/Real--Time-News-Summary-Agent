# Real--Time-News-Summary-Agent
Introduction:
  A Real-Time News Summary Web Application built using Flask (Python) that fetches the latest news headlines using the GNews API and displays them in a clean and simple user interface. Users can quickly view trending news headlines and open full articles directly from trusted news sources.

Project Overview:
 This project collects real-time news headlines from an external news API and displays them dynamically on a web page.

The application:
 1) Fetches live news using API requests
 2) Displays headlines and descriptions
 3) Provides direct links to read the complete article
 4) Uses Flask backend with HTML frontend

Features:
 1) Real-time news fetching using API
 2) Clean and simple UI design
 3) Clickable links to full articles
 4) Country-specific news (India)
 5) Easy to customize categories and filters
 6) Lightweight Flask application

Technologies Used:
 1) Python
 2) Flask
 3) HTML5
 4) CSS3

Requests Library:
  GNews API

Project Structure:
Real-Time-News-Summary/
│
├── app.py                # Flask backend application
├── requirements.txt      # Python dependencies
│
├── templates/
│      └── index.html     # Frontend UI template
│
└── README.md             # Project documentation

Installation and Setup:
  Follow these steps to run the project locally.

1️) Clone Repository:
git clone https://github.com/your-username/real-time-news-summary.git
cd real-time-news-summary

2️) Create Virtual Environment (Recommended)
Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

3️) Install Dependencies:
pip install -r requirements.txt

4️) Add API Key:
Get your free API key from GNews.

Open app.py and replace:
API_KEY = "YOUR_API_KEY"
with your actual API key.

5️) Run Application:
python app.py

6️) Open Browser:
Visit:
http://127.0.0.1:5000/

Author:
Shreenidhi E
