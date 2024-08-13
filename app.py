from flask import Flask

# create an instance of the Flask Class

app = Flask(__name__)

#Define a route
@app.route('/')
def order_date():
    return 'Hello, world'

#Run the app
if __name__ == '__main__':
    app.run()