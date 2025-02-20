from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import pandas as pd
import os

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb+srv://pgikiru:EXpJzQttfpcKUWr1@cluster0.8cqax.mongodb.net")
db = client.surveyDB
collection = db.user_data

# User Class
class User:
    def __init__(self, age, gender, income, expenses):
        self.age = int(age)
        self.gender = gender
        self.income = float(income)
        self.expenses = {k: float(v) for k, v in expenses.items()}
    
    def to_dict(self):
        return {
            "age": self.age,
            "gender": self.gender,
            "income": self.income,
            "expenses": self.expenses
        }

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
        age = request.form.get("age")
        gender = request.form.get("gender")
        income = request.form.get("income")
        
        expenses = {
            "utilities": request.form.get("utilities", 0),
            "entertainment": request.form.get("entertainment", 0),
            "school_fees": request.form.get("school_fees", 0),
            "shopping": request.form.get("shopping", 0),
            "healthcare": request.form.get("healthcare", 0)
        }
        
        user = User(age, gender, income, expenses)
        collection.insert_one(user.to_dict())
        
        return "Survey submitted successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/export')
def export_data():
    try:
        records = list(collection.find({}, {"_id": 0}))
        df = pd.DataFrame(records)
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/survey_data.csv", index=False)
        return "Data exported successfully!"
    except Exception as e:
        return f"Export Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
