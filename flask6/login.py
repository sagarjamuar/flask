from flask import Flask, render_template, request

app = Flask("myapp6")

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if "username" in request.form and "password" in request.form:
        username = request.form['username']
        password = request.form['password']
        if username == "user" and password == "password":
            credentials = "Welcome user"
        else:
            credentials = "Incorrect username and/or password"
        return render_template('login.html', credentials = credentials)
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)