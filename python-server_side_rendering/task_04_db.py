from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return None

def read_db():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        products = [dict(zip(columns, row)) for row in rows]
        conn.close()
        return products
    except sqlite3.DatabaseError as e:
        print(e)
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_db()
    else:
        products = None
        error = "Wrong source. Please use 'json', 'csv', or 'sql'."
        return render_template('product_display.html', error=error)
    
    if products is None:
        error = "Error reading data. Please check data source."
        return render_template('product_display.html', error=error)

    if product_id:
        product = next((p for p in products if int(p["id"]) == product_id), None)
        if product is None:
            error = "Product not found."
            return render_template('product_display.html', error=error)
        return render_template('product_display.html', products=[product])
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
