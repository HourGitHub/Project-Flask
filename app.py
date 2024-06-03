from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Create the database instance
db = SQLAlchemy(app)

# Define a User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Define the route for the homepage
@app.route('/')
def index():
    return render_template('base.html')

# Define the route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('views/login.html')

# Define the route for logging out
@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    return render_template('views/cart.html')

@app.route('/payment')
def payment():
    return render_template('views/payment.html')

if __name__ == '__main__':
    with app.app_context():
        # Create the database tables
        db.create_all()
    
    # Run the app
    app.run(debug=True)
