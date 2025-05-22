
from flask import Flask, request, jsonify, render_template
import spacy
import re

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

DAYS = {
    "monday": "Monday",
    "tuesday": "Tuesday",
    "wednesday": "Wednesday",
    "thursday": "Thursday",
    "friday": "Friday",
    "saturday": "Saturday",
    "sunday": "Sunday",
    "weekends": ["Saturday", "Sunday"],
    "weekdays": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
}

def parse_availability(text):
    text = text.lower()
    results = []
    doc = nlp(text)

    for sent in doc.sents:
        sentence = sent.text
        for day_key, day_val in DAYS.items():
            if day_key in sentence:
                start, end = "10:00", "16:00"

                if "morning" in sentence:
                    start, end = "08:00", "12:00"
                elif "afternoon" in sentence:
                    start, end = "13:00", "17:00"
                elif "evening" in sentence:
                    start, end = "17:00", "20:00"
                elif "all day" in sentence:
                    start, end = "08:00", "18:00"
                elif "after" in sentence:
                    match = re.search(r"after (\d{1,2})(am|pm)?", sentence)
                    if match:
                        hour = int(match.group(1))
                        if match.group(2) == "pm" and hour != 12:
                            hour += 12
                        start = f"{hour:02d}:00"
                        end = "20:00"

                if isinstance(day_val, list):
                    for d in day_val:
                        results.append({"day": d, "start": start, "end": end})
                else:
                    results.append({"day": day_val, "start": start, "end": end})

    return results

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/parse', methods=['POST'])
def api_parse():
    data = request.json
    text = data.get("text", "")
    results = parse_availability(text)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
