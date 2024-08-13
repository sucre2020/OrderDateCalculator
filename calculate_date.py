from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

def get_next_order_date(current_order_date, days_to_hold):
    try:
        order_date = datetime.strptime(current_order_date, '%m/%d/%Y')
        new_order_date = order_date + timedelta(days=days_to_hold)
        return new_order_date.strftime('%m/%d/%Y')
    except ValueError:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        current_order_date = request.form['current_order_date']
        days_to_hold = int(request.form['days_to_hold'])
        next_order_date = get_next_order_date(current_order_date, days_to_hold)
        if next_order_date:
            return render_template('result.html', next_order_date=next_order_date, days_to_hold=days_to_hold)
        else:
            return render_template('index.html', error=True)
    return render_template('index.html', error=False)

if __name__ == "__main__":
    app.run(debug=True)