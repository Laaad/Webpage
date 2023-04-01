from flask import Flask, request, render_template, redirect, url_for, flash
import smtplib
import os

MY_EMAIL = 'ladan.rb@gmail.com'
PASSWORD = os.getenv('PASSWORD')

app = Flask(__name__)
app.config['SECRET_KEY']= os.getenv('FLASK_SECRET_KEY')

def mail_to(name, email, message):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Ladan's Website "
                                                                   f"\n\n From:{name} \n\n Email:{email}\n\n"
                                                                   f"Message: {message}")
    connection.close()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=["POST"])
def contact():
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        mail_to(name, email, message)
        return 'Your Message Sent Successfully'


if __name__ == "__main__":
    app.run(port=5001)

