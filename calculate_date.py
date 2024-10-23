from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

# Function to calculate the next order date
def get_next_order_date(current_order_date, days_to_hold):
    try:
        order_date = datetime.strptime(current_order_date, '%m/%d/%Y')
        new_order_date = order_date + timedelta(days=days_to_hold)
        return new_order_date.strftime('%m/%d/%Y')
    except ValueError:
        return None

# Function to calculate the total after discount
def calculate_total(order_amount, discount_amount):
    try:
        total = (order_amount - discount_amount / 100 * order_amount)
        # total = order_amount - discount_amount
        return round(total, 2)
    except ValueError:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetching form inputs
        current_order_date = request.form.get('current_order_date')
        days_to_hold = request.form.get('days_to_hold')
        order_amount = request.form.get('order_amount')
        discount_amount = request.form.get('discount_amount')
        
        # Calculate the next order date if input is provided
        next_order_date = None
        if current_order_date and days_to_hold:
            next_order_date = get_next_order_date(current_order_date, int(days_to_hold))
        
        # Calculate total after discount if input is provided
        total = None
        if order_amount and discount_amount:
            total = calculate_total(float(order_amount), float(discount_amount))
        
        # Render the result page with both calculations
        return render_template(
            'result.html', 
            next_order_date=next_order_date, 
            days_to_hold=days_to_hold, 
            total=total, 
            order_amount=order_amount, 
            discount_amount=discount_amount
        )
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
