# Import the tools we need
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Create the main brain of our web application
app = Flask(__name__)

# --- DATABASE SETUP ---
# Configure the location of the database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestbook.db'
# Create the database object
db = SQLAlchemy(app)

# --- DATABASE MODEL ---
# Create the blueprint for our guestbook entries
class GuestbookEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)

# --- ROUTES ---
# This is the route for the homepage.
# We've added 'methods=['GET', 'POST']' to allow the form to send data.
@app.route('/', methods=['GET', 'POST'])
def home():
    # This 'if' statement checks if the user is submitting the form
    if request.method == 'POST':
        # Get the data from the form
        entry_name = request.form.get('name')
        entry_message = request.form.get('message')

        # Create a new entry for our database
        new_entry = GuestbookEntry(name=entry_name, message=entry_message)

        # Add and save the new entry to the database
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/')

    # If the user is just visiting the page, just show the HTML
    return render_template('index.html')

# This line allows us to run the app
if __name__ == '__main__':
    app.run(debug=True)
