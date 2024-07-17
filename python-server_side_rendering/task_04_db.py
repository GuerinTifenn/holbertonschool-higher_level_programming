#!/usr/bin/python3
"""
Testing different URLs in the browser:
- `http://localhost:5000/products?source=json`:
Displays products from the JSON file.
- `http://localhost:5000/products?source=csv`:
Displays products from the CSV file.
- `http://localhost:5000/products?source=sql`:
Displays products from the SQLite database.
- `http://localhost:5000/products?source=xml`:
Displays the error message "Wrong source".
- `http://localhost:5000/products?source=json&id=1`:
Displays details of the product with ID 1 from the JSON file.
- `http://localhost:5000/products?source=csv&id=3`:
Displays the error message "Product not found" if the ID does not exist.
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    items = data.get('items', [])
    return render_template('items.html', items=items)


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products


def read_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    products = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "category": row[2],
             "price": row[3]} for row in products]


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        data = read_sqlite('products.db')
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        product = next((item for item in data
                        if str(item['id']) == product_id), None)
        if not product:
            return render_template('product_display.html',
                                   error="Product not found")
        data = [product]

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
