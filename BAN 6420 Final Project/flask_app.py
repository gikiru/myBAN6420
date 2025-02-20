from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://pgikiru:EXpJzQttfpcKUWr1@cluster0.8cqax.mongodb.net/")
db = client.surveyDB
collection = db.user_data  # Collection to store survey data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    user_data = {
        "age": int(request.form['age']),
        "gender": request.form['gender'],
        "income": float(request.form['income']),
        "expenses": {
            "utilities": float(request.form['utilities']),
            "entertainment": float(request.form['entertainment']),
            "school_fees": float(request.form['school_fees']),
            "shopping": float(request.form['shopping']),
            "healthcare": float(request.form['healthcare']),
        }
    }

    # Insert into MongoDB
    collection.insert_one(user_data)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
