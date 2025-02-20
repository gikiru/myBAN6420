README
Survey Data Collection & Analysis Tool
This project is a Flask-based web application designed to collect user survey data, store it in MongoDB, process it in Python, and visualize insights using Jupyter Notebook. The tool is built to analyze income and spending patterns in preparation for a healthcare product launch.

Features:
•	A simple Web Form (Flask): Collects user details (Age, Gender, Income, Expenses).
•	MongoDB Storage: Saves survey responses securely.
•	Data Processing: Converts stored data into CSV format.
•	Data Visualization: Analyzes and visualizes trends in Jupyter Notebook.
•	Deployment: Hosted on Render, ensuring accessibility. https://myban6420.onrender.com

Prerequisites:
•	Ensure you have the following installed:  
•	Python 3.8+
•	MongoDB (Local or Atlas)
•	pip (Python package manager)
•	Git

Instructions:
•	Clone the Repository
•	Create and activate a python virtual environment to run the flask_app
•	Install dependencies: pip install -r requirements.txt
•	Configure the database connection by updating the MongoDB URI
•	Run the flask_app for data collection and exporting the data
•	Run the analysis.ipynb to visualize the data from the survey_data notebook
•	Retrieve the images from the visualizations folder of the project directory for use in making your PowerPoint presentation

For deployment on Render
•	The project has the following files: requirements.txt for dependencies and Procfile for Gunicorn
•	Link to deployed app on render: https://myban6420.onrender.com/ 


Development tools used:
•	Flask, Gunicorn as backend
•	MongoDB as database
•	Pandas/Python for data processing
•	Matplotlib and Seaborn for visualization
•	App hosted on Render
