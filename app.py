from flask import Flask, render_template, request, session
from forex_python.converter import CurrencyRates
from decimal import Decimal


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
# RESPONSES_KEY = 'responses'

@app.route('/')
def home():
    
    # session[RESPONSES_KEY] = []
    return render_template('index.html')
    

@app.route('/answer', methods=['POST'])
def show_converted_amount():
    first_input = request.form['first_input'].upper()
    second_input = request.form['second_input'].upper()
    third_input = request.form['third_input']
    
    # session[RESPONSES_KEY].append(first_input)
    # session[RESPONSES_KEY].append(second_input)
    # session[RESPONSES_KEY].append(third_input)
    # responses = session.get(RESPONSES_KEY)
    c = CurrencyRates()
    rates = c.convert(f"{first_input}", f"{second_input}", Decimal(third_input))
    # converted_amount = c.convert(f"{first_input}", f"{second_input}", third_input)
    # responses = session[RESPONSES_KEY]

    return render_template('answer.html', rates = rates)

    

    #declaration of the instance of the class CurrencyRates()
    
    #  c.get_rate('USD', 'EUR')
    # c.convert('USD', 'EUR', 1290192)