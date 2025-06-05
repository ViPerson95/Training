from flask import Flask, render_template, request, redirect, url_for, g
import random
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
DATABASE = 'registrations.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    event_name = request.args.get('event') or request.form.get('event', '')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS registrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                event TEXT
            )
        ''')
        db.execute(
            'INSERT INTO registrations (name, email, event) VALUES (?, ?, ?)',
            (name, email, event_name)
        )
        db.commit()
        return redirect(url_for('index'))
    return render_template('register.html', event_name=event_name)

if __name__ == '__main__':
    app.run(debug=True)
