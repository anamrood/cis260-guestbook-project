# Import the tools we need from the Flask package
from flask import Flask, render_template

# Create the main brain of our web application
app = Flask(__name__)

# This is the route for the homepage.
@app.route('/')
def home():
    # This function's only job is to display our HTML page to the user.
    return render_template('index.html')

# This line allows us to run the app
if __name__ == '__main__':
    app.run(debug=True)