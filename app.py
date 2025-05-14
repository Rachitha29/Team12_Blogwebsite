from flask import Flask, render_template, request, redirect, flash, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for flash messages

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if not name or not email or not message:
            flash("Please fill out all fields.", "error")
            return redirect(url_for('contact'))

        # Optional: Save to a file (could use DB instead)
        with open("messages.txt", "a") as f:
            f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

        flash("Thank you for your message!", "success")
        return redirect(url_for('contact'))

    return render_template("contact.html")

