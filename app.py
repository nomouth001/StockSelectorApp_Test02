from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user = request.args.get('user', 'default')
    with open('sp500.csv', encoding='utf-8') as f:
        tickers = [line.strip().split(',') for line in f.readlines()[1:]]
    try:
        with open(f'selected_{user}.txt') as f:
            selected = [line.strip() for line in f if line.strip()]
    except:
        selected = []
    if request.method == 'POST':
        selected = request.form.getlist('tickers')
        with open(f'selected_{user}.txt', 'w') as f:
            f.write('\n'.join(selected))
    return render_template('index.html',
                           user=user,
                           all_tickers=tickers,
                           selected=selected)
