from flask import Flask, render_template, request
import webbrowser
import threading

app = Flask(__name__)

exchange_rate = {
    'USD': 1.00,
    'INR': 85.60,
    'EUR': 0.90,
    'YUAN': 7.21,
    'YEN': 145.94,
    'WON': 1401.13,
    'DIRHAM': 3.67,
    'POUND': 0.75
}

def currency_converter(amount, from_currency, to_currency):
    if (from_currency not in exchange_rate) or (to_currency not in exchange_rate):
        return None
    amount_in_usd = amount / exchange_rate[from_currency]
    return amount_in_usd * exchange_rate[to_currency]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_curr = request.form['from_currency'].upper()
            to_curr = request.form['to_currency'].upper()
            result = currency_converter(amount, from_curr, to_curr)
            if result is None:
                error = "Unsupported currency."
        except ValueError:
            error = "Invalid amount entered."

    # Pass result, error, and currencies list to template
    return render_template('index.html', result=result, error=error, currencies=exchange_rate.keys())

if __name__ == '__main__':
    app.run(debug=True)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run()

# MIT License
# Copyright (c) 2025 ARI R

"""
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction..."""