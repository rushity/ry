from flask import Flask, render_template, request
import cl  # Import the logic from cl.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve data from the form
    total_leaves = int(request.form['total_leaves'])
    leaves_per_month = int(request.form['leaves_per_month'])
    months = int(request.form['months'])

    # Retrieve monthly leaves from the form
    monthly_leaves = []
    for i in range(months):
        monthly_leaves.append(int(request.form[f'leaves_month_{i+1}']))

    # Call the function from cl.py with the provided data
    table_data = cl.calculate_leaves(total_leaves, leaves_per_month, months, monthly_leaves)

    return render_template('result.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)
