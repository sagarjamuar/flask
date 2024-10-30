from flask import Flask, render_template

app = Flask(__name__)

# Predefined list of users
users = [
    {'name': 'Sagar', 'age': 21, 'city': 'Pune'},
    {'name': 'Akshat', 'age': 24, 'city': 'Bhilai'},
    {'name': 'Vinayak', 'age': 22, 'city': 'Delhi'}
]

@app.route('/users')
def display_users():
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
