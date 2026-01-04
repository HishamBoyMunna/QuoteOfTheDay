from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_random_quote():
    url = "https://dummyjson.com/quotes/random"
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        data = response.json()
        return {
            "text": data.get("quote")
            "author": data.get("author")
        }
    except Exception as e:
    
