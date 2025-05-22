
# 🗓️ NLP-Powered Availability Calendar (Flask + spaCy)

This is a simple Flask web application that uses **spaCy NLP** to extract availability information from natural language text and displays it on a calendar using FullCalendar.js.

## 🔧 Features

- Parse phrases like:
  - `"I'm free Monday mornings and Friday after 2pm"`
  - `"Available weekends and Tuesday all day"`
- Returns structured time slots (day, start, end)
- Renders them on an interactive weekly calendar

## 🚀 Deployment on Render

1. Fork or clone this repo to your GitHub
2. Create a free account at [Render.com](https://render.com)
3. Click **New Web Service** → Select your repo
4. Ensure the platform detects `render.yaml` (auto-deploy config)
5. Click **Deploy**

## 🧠 Requirements

- Python 3.8+
- Flask
- spaCy
- `en_core_web_sm` (automatically downloaded on deploy)

## 🖥️ Local Dev (Optional)

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
```

## ✨ Live Demo Preview

Once deployed, your Render URL will look like:
```
https://availability-calendar.onrender.com
```

---

Made with 💻 and ☕
