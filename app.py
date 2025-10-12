# Import the tools we need
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Create the main brain of our web application
app = Flask(__name__)

# --- DATABASE SETUP ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestbook.db'
db = SQLAlchemy(app)

# --- DATABASE MODEL ---
class GuestbookEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)

# --- ROUTES ---
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        entry_name = request.form.get('name')
        entry_message = request.form.get('message')
        new_entry = GuestbookEntry(name=entry_name, message=entry_message)
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/')

    # --- NEW CODE FOR THE 'READ' FEATURE ---
    # Get all the current entries from the database.
    entries = GuestbookEntry.query.all()
    # Pass the list of entries to the HTML template.
    return render_template('index.html', entries=entries)

# This line allows us to run the app
if __name__ == '__main__':
    app.run(debug=True)
