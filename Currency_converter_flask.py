from flask import Flask, render_template, request
import requests
import webbrowser
import threading

app = Flask(__name__)

# List of supported currencies
supported_currencies = ['USD', 'INR', 'EUR', 'CNY', 'JPY', 'KRW', 'AED', 'GBP']
# Mapped to common names: YUAN=CNY, YEN=JPY, WON=KRW, DIRHAM=AED, POUND=GBP

# Real-time currency conversion function
def currency_converter(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates'][to_currency]
    except Exception as e:
        print("API Error:", e)
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_curr = request.form['from_currency'].upper()
            to_curr = request.form['to_currency'].upper()

            # Validate currency
            if from_curr not in supported_currencies or to_curr not in supported_currencies:
                error = "Unsupported currency selected."
            else:
                result = currency_converter(amount, from_curr, to_curr)
                if result is None:
                    error = "Conversion failed. Try again later."

        except ValueError:
            error = "Invalid amount entered."

    return render_template('index.html', result=result, error=error, currencies=supported_currencies)

# Auto-open browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True)


# MIT License
# Copyright (c) 2025 ARI R

"""
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction..."""