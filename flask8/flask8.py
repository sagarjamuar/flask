from flask import Flask, render_template, request

app = Flask('myapp8')

feedbacks = []


@app.route('/feedback', methods = ['POST','GET'])
def feedback():
    if 'name' in request.form and 'feedback' in request.form:
        feedbacks.append({'name': request.form['name'], 'feedback': request.form['feedback']})
    return render_template('feedback.html', feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)