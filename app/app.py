from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product

main = Blueprint('main', __name__)

# 管理メニュー
@main.route('/')
def admin_menu():
    return render_template('menu.html')

# 商品一覧
@main.route('/products/view')
def view_products():
    products = Product.query.all()
    return render_template('view_products.html', products=products)

# 商品追加
@main.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name'].strip()
        price = request.form['price']
        if not name or not price:
            flash('商品名と価格は必須です。', 'error')
            return redirect(url_for('main.add_product'))
        try:
            price = float(price)
            if price < 0:
                raise ValueError('価格は正の値である必要があります。')
            new_product = Product(name=name, price=price)
            db.session.add(new_product)
            db.session.commit()
            flash('商品が正常に追加されました！', 'success')
            return redirect(url_for('main.view_products'))
        except ValueError as ve:
            flash(str(ve), 'error')
        except Exception as e:
            db.session.rollback()
            flash('エラーが発生しました。', 'error')
    return render_template('add_product.html')

# 商品編集
@main.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        name = request.form['name'].strip()
        price = request.form['price']
        if not name or not price:
            flash('商品名と価格は必須です。', 'error')
            return redirect(url_for('main.edit_product', product_id=product_id))
        try:
            price = float(price)
            if price < 0:
                raise ValueError('価格は正の値である必要があります。')
            product.name = name
            product.price = price
            db.session.commit()
            flash('商品情報が正常に更新されました！', 'success')
            return redirect(url_for('main.view_products'))
        except ValueError as ve:
            flash(str(ve), 'error')
        except Exception as e:
            db.session.rollback()
            flash('エラーが発生しました。', 'error')
    return render_template('edit_product.html', product=product)
