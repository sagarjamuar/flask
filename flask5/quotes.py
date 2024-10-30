from flask import Flask, render_template
import random

app = Flask("myapp5")

@app.route('/quote', methods=['GET'])
def quotes():
    quotes = ["Success is not final, failure is not fatal: It is the courage to continue that counts.", "The only limit to our realization of tomorrow is our doubts of today.", "Life is 10% what happens to us and 90% how we react to it.", "Believe you can and you're halfway there.", "Do not watch the clock; do what it does. Keep going.", "Happiness is not something ready-made. It comes from your own actions.", "If opportunity doesn’t knock, build a door."]
    quote = random.choice(quotes)
    return render_template("quotes.html", quote = quote)

if __name__ == '__main__':
    app.run(debug=True)
