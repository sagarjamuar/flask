from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature_converter():
    fahrenheit = None
    if request.method == 'POST':
        try:
            celsius = float(request.form['celsius'])
            fahrenheit = (celsius * 9/5) + 32
        except ValueError:
            fahrenheit = "Invalid input. Please enter a numeric value."
    return render_template('temperature.html', fahrenheit=fahrenheit)

if __name__ == '__main__':
    app.run(debug=True)
