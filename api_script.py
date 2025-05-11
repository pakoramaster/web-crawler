# Api script to look up articles from a dataset

# Run this command in terminal to install the required packages:
# pip install -r requirements.txt

# For GUI Interface go to: Go to http://localhost:30/docs

# Imports
import uvicorn
from fastapi import FastAPI
import pandas as pd
from datetime import date

# Loading the dataset form csv
data_file = "articles.xlsx"
df = pd.read_excel(data_file)

# Convert date column to datetime format (YYYY-MM-DD)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.date

# Initializing fastapi
app = FastAPI(title="CNN Articles API")

# Home page
@app.get("/")
def home():
    return {"message": "Welcome to the CNN Articles API!"}

# Function to get all articles
@app.get("/articles")
def get_articles():
    return df.to_dict(orient="records")

# Function to get articles by date
@app.get("/articles/date")
def get_articles_by_date(pub_date: date):
    filtered_df = df[df["Date"] == pub_date]
    return filtered_df.to_dict(orient="records")

# Function to get articles by keyword
@app.get("/articles/keyword")
def get_articles_by_keyword(keyword: str):
    keyword = keyword.lower()
    filtered_df = df[df["Title"].str.lower().str.contains(keyword) | df["Summary"].str.lower().str.contains(keyword)]
    return filtered_df.to_dict(orient="records")

# Function to get articles by category
@app.get("/articles/category")
def get_articles_by_category(category: str):
    filtered_df = df[df["Category"].str.lower() == category.lower()]
    return filtered_df.to_dict(orient="records")

# Starting api
uvicorn.run(app, host="localhost", port=30)