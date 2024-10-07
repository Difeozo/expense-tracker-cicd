from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

users = {}
transactions = []

@app.route('/')
def home():
    return 'Welcome to the Expense Tracker!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        if username not in users:
            users[username] = {'balance': 0, 'transactions': []}
            print(users)  # Debug: Print the users dictionary
            return redirect(url_for('home'))
        else:
            return 'User already exists!'
    return render_template('register.html')

@app.route('/add_balance/<username>', methods=['GET', 'POST'])
def add_balance(username):
    if request.method == 'POST':
        amount = float(request.form['amount'])
        if username in users:
            users[username]['balance'] += amount
            return redirect(url_for('balance', username=username))
        return 'User not found!'
    return render_template('add_balance.html', username=username)

@app.route('/balance/<username>')
def balance(username):
    if username in users:
        return f"{username}'s balance: {users[username]['balance']}"
    return 'User not found!'

@app.route('/transactions/<username>')
def transaction_history(username):
    if username in users:
        return f"{username}'s transaction history: {users[username]['transactions']}"
    return 'User not found!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    print("🚀 The Expense Tracker Application is now running!")  # Moved log statement here

// This is a test to trigger GitHub Actions

