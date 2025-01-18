from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import db, Product

main = Blueprint('main', __name__)

@main.route('/')
def admin_menu():
    return render_template('menu.html')

@main.route('/products/view')
def view_products():
    products = Product.query.all()
    return render_template('view_products.html', products=products)

@main.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = float(request.form['price'])
        db.session.commit()
        return redirect(url_for('main.view_products'))
    return render_template('edit_product.html', product=product)

@main.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        new_product = Product(name=name, price=price)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('main.view_products'))
    return render_template('add_product.html')
