from flask import Flask, render_template
import random
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    # Generate demo news articles
    news_items = []
    titles = [
        "Community Garden Expands",
        "Local Library Hosts Book Fair",
        "Neighborhood Cleanup Success",
        "Food Truck Festival Announced",
        "Youth Sports League Registration"
    ]
    descriptions = [
        "Join us this weekend to celebrate the new garden plots added to the community garden.",
        "A wide selection of books will be available for all ages and interests.",
        "Volunteers collected over 50 bags of trash in the annual cleanup event.",
        "Taste dishes from 15 local food trucks downtown this Saturday.",
        "Sign up now for the upcoming season of youth sports programs."
    ]

    for i in range(5):
        news_items.append({
            "title": titles[i],
            "description": descriptions[i],
            "date": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        })

    # Generate demo events
    event_names = [
        "Art in the Park",
        "Charity Fun Run",
        "Outdoor Movie Night",
        "Community Potluck",
        "Local Craft Market"
    ]
    events = []
    for name in event_names:
        events.append({
            "name": name,
            "date": (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d"),
            "location": random.choice(["Main Street", "Central Park", "Town Hall", "Riverside Plaza"]) 
        })

    return render_template('index.html', news_items=news_items, events=events)

if __name__ == '__main__':
    app.run(debug=True)
