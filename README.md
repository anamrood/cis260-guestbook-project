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
**Next Step:** Begin coding the 'Create' feature next week.

**Week 5 (September 22 - 28)**
Goal: I created the initial starting structure of the Flask application and learned the Git workflow.

Accomplished:

Set up the project's file structure by creating the app.py file and a templates folder containing index.html.

Wrote the initial Flask code in app.py to define a route for the homepage and render the index.html template.

Successfully ran the web server for the first time from the terminal using the py app.py command.  **(py app.py)**

Confirmed the application was working by opening http://127.0.0.1:5000 in a web browser and viewing the basic HTML form.

Initialized the local Git repository using the git init command.

Used the built-in 'Publish to GitHub' feature in VS Code to automatically connect the local repository to the remote one on GitHub.

Learned and executed the full Git workflow to save my work: preparing files with git add ., saving a snapshot with git commit -m "...", and uploading to GitHub with git push. **( git add . , git commit -m "..." , git push)**

**Next Step:** Connect the form to the database to save user messages.

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

**Next Step:** Build the 'Read' feature to display the saved messages on the page.

### **Week 7 (October 6 - October 12)**
**Goal:** Create the Read feature to be able to see messages on the website. 
**Accomplished:** 
1. First, I went into my app.py file and changed the home() function. I added a line that uses GuestbookEntry.query.all() to pull all the saved messages out of the database and put them into a list.

2. Then, I had to update the return render_template() line so it would pass that list of messages over to my index.html page, making the data available to the front-end.

3. After that, I switched over to the index.html file and added a new "Messages" section below the form.

4. The interesting part was using a Jinja2 for loop, which looks like {% for entry in entries %}, to go through each message that the Python file sent over.

5. Inside that loop, I used placeholders like {{ entry.name }} and {{ entry.message }} to actually print out the name and message for each post as a new list item.

6. To finish up, I ran the app with py app.py and confirmed that all the old messages I had submitted were finally there on the page.

Next Step: Prepare for the Midterm Presentation.

### **Week 8 (October 13 - October 19)**
**Goal:** Prepare for the Midterm Presentation 
**Accomplished:** The core functionality such as the Create and Read features for the dynamic guestbook web application is working together. Prepared the live demo to showcase the guestbook web application functions properly.  
**Next Step:**  Style the front-end with CSS.

### **Week 9 (October 20 - 26)**
* **Goal:** Apply CSS styles provided by the professor and understand how they work.
* **Accomplished (Oct 25):**
    1. Noticed styles weren't applying. Realized my local repository was missing the `static` folder and `styles.css` file added by the professor on GitHub.
    2. Tried to use **`git pull`** but got an error because I had unsaved local changes in `index.html` (where I had added the `<link>` tag).
    3. Resolved the conflict using the following 3-step process in the terminal:
        * Temporarily hid my local changes with **`git stash`**.
        * Successfully downloaded the professor's changes (including the `static` folder and `styles.css`) using **`git pull`**.
        * Checked `index.html` and saw the professor had **also** added the correct `<link>` tag, so my stashed change was no longer needed. I discarded it with **`git stash drop`**.
    4. Confirmed that the CSS styles are now correctly applied to the application.
    5. I ran the app with py app.py and noticed that the website looked different from before with the new css changes that were added.
* **Next Step:** Continue studying the `styles.css` file and experiment with changes (Week 10).

### **Week 10 (October 27 - November 2)**
* **Goal:** Study and experiment with the provided CSS.
* **Accomplished (Oct 31):** Studied the `styles.css` file to understand its structure. I experimented with the code by making three main changes:
    1.  I changed the `.header h1` color to `var(--accent)`, which successfully turned the main title green.
    2.  I changed the `.entry-name` color to `var(--brand)`, which successfully turned the names in the message list blue.
    3.  I then tried to change the submit button's background to green, which turned into a long troubleshooting session.
* **Troubleshooting the Button:**
    * The button remained white despite my changes. I confirmed my `styles.css` and `index.html` files were saved and the server was running the new code.
    * The terminal showed a `200` success code, but my browser was still loading a cached, broken version.
    * After trying `Ctrl+Shift+R` and Incognito, I realized the problem was CSS "specificity." The browser's default style was overriding my class.
    * **The Fix:** I solved this by making my rule `button.btn-primary` and adding `background: green !important;`. This finally forced the browser to apply my custom style.
* **Next Step:** Begin working on back-end error handling.

### **Week 11 (November 3 - 9)**
* **Goal:** Refine the back-end with error handling.
* **Accomplished (Nov 9):** Implemented server-side validation to prevent empty submissions. I added a `SECRET_KEY` to `app.py` and used the `flash()` function to send an error message if the name or message fields are empty. I also updated `index.html` to display these flash messages, which correctly use the `.flash-error` style from the CSS.
* **Next Step:** Begin final documentation review and updates for the final presentation.