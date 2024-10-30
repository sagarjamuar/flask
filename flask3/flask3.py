from flask import Flask, render_template, request

app = Flask('myapp3')

@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    result = None
    if request.method == 'POST':
        try:
            first = float(request.form['first'])
            second = float(request.form['second'])
            result = first + second
        except ValueError:
            result = "Invalid input. Please enter a numeric value"
    return render_template("calculator.html", result = result)

if __name__ == '__main__':
    app.run(debug=True)