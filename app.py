from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None

    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    error = 'Cannot divide by zero.'
                else:
                    result = num1 / num2
            else:
                error = 'Invalid operation.'

        except ValueError:
            error = 'Invalid input. Please enter numeric values.'

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(port=6007)

