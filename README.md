# Community News and Events

This project provides a simple Flask-based web application to share community news and upcoming events.
When the app starts, it randomly generates demo news articles and events so you can see sample content right away.

## Setup

1. Create a virtual environment and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000`.

The default styles use a green color palette and subtle geometric pattern inspired by Islamic art.

## Project Structure

```
.
├── app.py           # main Flask application
├── requirements.txt # Python dependencies
├── static/          # CSS and other static assets
└── templates/       # HTML templates
```

When you run `app.py`, Flask looks in the `templates/` folder for the HTML files
and serves assets from the `static/` folder. The `index` route in `app.py`
generates sample news and events each time the page loads so you can see how the
site will look with real content.
