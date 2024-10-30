from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        # Get the new task from the form
        task = request.form.get('task')
        if task:
            tasks.append(task)  # Add task to the list
    return render_template('todo.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
