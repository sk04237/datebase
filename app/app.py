from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

# Flaskアプリケーションの設定
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')  # セキュリティ用の秘密鍵

# データベースの初期化
db = SQLAlchemy(app)

# 商品データのモデルを定義
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)  # 商品名は重複不可
    price = db.Column(db.Float, nullable=False)  # 商品価格

    def __repr__(self):
        return f'<Product {self.name}>'

# 管理メニュー
@app.route('/')
def admin_menu():
    return render_template('menu.html')

# 商品一覧を表示
@app.route('/products/view')
def view_products():
    products = Product.query.all()  # データベースから全てのデータを取得
    return render_template('view_products.html', products=products)

# 商品を追加
@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':  # フォームが送信された場合
        name = request.form['name'].strip()  # 商品名を取得
        price = request.form['price']  # 価格を取得

        if not name or not price:  # 入力チェック
            flash('商品名と価格は必須です。', 'error')
            return redirect(url_for('add_product'))

        try:
            price = float(price)  # 価格を数値に変換
            if price < 0:  # 価格が負の値か確認
                raise ValueError('価格は正の値である必要があります。')

            new_product = Product(name=name, price=price)  # 新しい商品を作成
            db.session.add(new_product)  # データベースに追加
            db.session.commit()  # 変更を保存
            flash('商品が正常に追加されました！', 'success')
            return redirect(url_for('view_products'))
        except ValueError as ve:
            flash(str(ve), 'error')
        except IntegrityError:
            db.session.rollback()
            flash('商品名が重複しています。別の商品名を使用してください。', 'error')

    return render_template('add_product.html')

# 商品を編集
@app.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)  # 商品が存在しない場合404エラー

    if request.method == 'POST':  # フォームが送信された場合
        name = request.form['name'].strip()
        price = request.form['price']

        if not name or not price:  # 入力チェック
            flash('商品名と価格は必須です。', 'error')
            return redirect(url_for('edit_product', product_id=product_id))

        try:
            price = float(price)
            if price < 0:
                raise ValueError('価格は正の値である必要があります。')

            product.name = name
            product.price = price
            db.session.commit()  # 変更を保存
            flash('商品情報が正常に更新されました！', 'success')
            return redirect(url_for('view_products'))
        except ValueError as ve:
            flash(str(ve), 'error')
        except IntegrityError:
            db.session.rollback()
            flash('商品名が重複しています。別の商品名を使用してください。', 'error')

    return render_template('edit_product.html', product=product)

# アプリケーションのエントリーポイント
if __name__ == '__main__':
    app.run(debug=True)
