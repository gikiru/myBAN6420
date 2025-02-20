import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://pgikiru:EXpJzQttfpcKUWr1@cluster0.8cqax.mongodb.net/")
db = client.surveyDB
collection = db.user_data

# Fetch data from MongoDB
data = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB's default "_id" field

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert nested "expenses" dictionary into separate columns
expenses_df = df.pop("expenses").apply(pd.Series)
df = pd.concat([df, expenses_df], axis=1)

# Save to CSV
df.to_csv("survey_data.csv", index=False)

print("Data successfully exported to survey_data.csv")
