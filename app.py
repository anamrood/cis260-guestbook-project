# Import the new 'flash' tool and 'redirect'
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

# Create the main brain of our web application
app = Flask(__name__)

# --- NEW SECRET KEY ---
# This is required for flash messages to work
app.config['SECRET_KEY'] = 'a_super_secret_key_that_you_should_change'

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

        # --- NEW ERROR HANDLING LOGIC ---
        if not entry_name or not entry_message:
            # If either field is empty, flash an error message
            flash("Name and message cannot be empty!", "error")
        else:
            # Otherwise, save the data to the database
            new_entry = GuestbookEntry(name=entry_name, message=entry_message)
            db.session.add(new_entry)
            db.session.commit()
            return redirect('/')

    # Get all entries from the database
    entries = GuestbookEntry.query.all()
    # Pass the list of entries to the HTML template
    return render_template('index.html', entries=entries)

# This line allows us to run the app
if __name__ == '__main__':
    app.run(debug=True)
