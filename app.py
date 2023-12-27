from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = [
    {"product_no": "PTN123456", "description": "Smart Phone X", "cost": 2499, "image": "product1.jpg", "categories": "Electronics"},
    {"product_no": "KTB789012", "description": "Modern Cutlery Set", "cost": 349, "image": "product2.jpg", "categories": "Kitchenware"},
    {"product_no": "SPO345678", "description": "Children's Bicycle", "cost": 599, "image": "product3.jpg", "categories": "Sports and Outdoor"},
    {"product_no": "SGS567890", "description": "Portable Bluetooth Speaker", "cost": 149, "image": "product4.jpg", "categories": "Audio and Visual Systems"},
    {"product_no": "MBY234567", "description": "Office Chair", "cost": 899, "image": "product5.jpg", "categories": "Furniture"},
    {"product_no": "SPF901234", "description": "Fitness Tracker", "cost": 179, "image": "product6.jpg", "categories": "Sports and Fitness"},
    {"product_no": "MDA456789", "description": "Sunglasses", "cost": 129, "image": "product7.jpg", "categories": "Fashion and Accessories"},
    {"product_no": "BYZ678901", "description": "High-Performance Laptop", "cost": 4999, "image": "product8.jpg", "categories": "Computers and Software"},
    {"product_no": "MGI123456", "description": "Floral Print Dress", "cost": 279, "image": "product9.jpg", "categories": "Fashion and Apparel"},
    {"product_no": "ETK789012", "description": "Mini Digital Camera", "cost": 379, "image": "product10.jpg", "categories": "Electronics"},
]

@app.route('/')
def home():
    return render_template('homepage.html', products=products)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('q', '')
    results = [p for p in products if query.lower() in str(p).lower()]

    if request.method == 'POST':
        return redirect(url_for('search_results', query=query))

    return render_template('search.html', results=results, query=query)

@app.route('/search_results/<query>')
def search_results(query):
    results = [p for p in products if query.lower() in str(p).lower()]
    return render_template('search.html', results=results, query=query)

@app.route('/product/<string:product_no>')
def product_detail(product_no):
    product = next((p for p in products if p['product_no'] == product_no), None)
    return render_template('detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
