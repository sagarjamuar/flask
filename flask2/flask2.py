from flask import Flask, render_template

app = Flask("myapp2")

@app.route("/bio")
def bio():
    my_bio = {
        "name": "sagar",
        "age": "21",
        "hobbies": ["coding", "singing", "dancing"]
    }
    return render_template("bio.html", bio = my_bio)

if __name__=='__main__':
    app.run(debug=True)