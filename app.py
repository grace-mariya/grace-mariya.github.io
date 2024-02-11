from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail setup
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Use your mail server's port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'gracethakkolkaran29@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'gr@ce2901'  # Replace with your email password

mail = Mail(app)


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Add your login logic here

        # Send comments and queries to the provided email after login
        send_comment_to_email(email)
        send_queries_to_email(email)

        return redirect('/index')

    return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def add_comment():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        send_comment_to_email(name, comment)
        return redirect('/index')
    return render_template('index.html')

@app.route('/submit_quarries', methods=['POST'])
def submit_quarries():
    quarries = request.form['Quarries']
    send_queries_to_email(quarries)
    flash('Quarry successfully submitted!', 'success')
    return redirect('/index')

def send_comment_to_email(name, comment):
    subject = 'New Comment'
    body = f"Name: {name}\nComment: {comment}"
    send_email(subject, body)

def send_queries_to_email(queries):
    subject = 'New Query'
    body = f"Queries: {queries}"
    send_email(subject, body)

def send_email(subject, body):
    msg = Message(subject, recipients=['gracethakkolkaran29@gmail.com'])  # Replace with your destination email
    msg.body = body
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
