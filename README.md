# This is your README file.

I have uploaded this for you, it is customary to have a README file within GitHub to insure that there is some documentation. Please let me know if you needed any other help. Also this is written in a language called "Markdown". I have linked it here [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

Please let me know if you needed any help. - Md Ali

Weekly Development Log

**Week 1 (August 25-31)**

-Goal: Finalize a project idea and plan.
-Accomplished: Decided on the 'Dynamic Guestbook Web Application' project and created a 15-week timeline. 

**Week 2 (September 1 - 7)**

-Goal: Create and submit the formal project proposal.
-Accomplished: Wrote and submitted the project proposal by the September 5th deadline.

**Week 3 (September 8 - 14)**

-Goal: Install all necessary software for the project.
-Accomplished: Installed Python, Visual Studio Code, and Git.

**Week 4 (September 15 - 21)**

-Goal: Create the project repository and learn the basics of Flask.
-Accomplished: Created the public GitHub repository. Learned the core concepts of Flask (`app.py`, routes, templates) in preparation for our first check-in.
-Next Step:** Begin coding the 'Create' feature next week.

**Week 5 (September 22 - 28)**
Goal: I created the initial starting structure of the Flask application and learned the Git workflow.

Accomplished:

Set up the project's file structure by creating the app.py file and a templates folder containing index.html.

Wrote the initial Flask code in app.py to define a route for the homepage and render the index.html template.

Successfully ran the web server for the first time from the terminal using the py app.py command.

Confirmed the application was working by opening http://127.0.0.1:5000 in a web browser and viewing the basic HTML form.

Initialized the local Git repository using the git init command.

Used the built-in 'Publish to GitHub' feature in VS Code to automatically connect the local repository to the remote one on GitHub.

Learned and executed the full Git workflow to save my work: preparing files with git add ., saving a snapshot with git commit -m "...", and uploading to GitHub with git push.

Next Step: Connect the form to the database to save user messages.

### **Week 6 (September 29 - October 5)**
* **Goal:** Make the guestbook form functional by connecting it to the database.
* **Accomplished:**
    1.  Installed the database package by running **`py -m pip install flask-sqlalchemy`** in the terminal.
    2.  Updated **`index.html`** by changing the `<form>` tag to `<form method="POST">` to allow it to send data.
    3.  Modified **`app.py`** to include the SQLAlchemy configuration, the `GuestbookEntry` data model, and the back-end logic to handle `POST` requests and save the form data to the database using `db.session.commit()`.
    4.  Created a temporary script, **`create_db.py`**, to initialize the database.
    5.  Ran the script from the terminal using **`py create_db.py`**, which successfully created the `guestbook.db` file with the code
     from app import app, db

with app.app_context():
    db.create_all()

print("Database created successfully!").
    6.  Finally, I tested the main application by running **`py app.py`** and confirmed that submitting the form saves the data without errors.

* **Next Step:** Build the 'Read' feature to display the saved messages on the page.
