# 商品管理アプリケーション

このプロジェクトは、Flaskを使用して構築された簡単な商品管理アプリケーションです。商品の登録、閲覧、編集、削除などの基本的な機能を提供します。

## 主な機能

1. **管理メニュー**:
   - 商品一覧画面、新規登録画面へのナビゲーション。

2. **商品一覧の表示**:
   - 登録済み商品のリストを表示します。
   - 商品ごとに編集リンクが表示されます。

3. **新規商品の登録**:
   - 商品名と価格を入力して、新しい商品を登録します。

4. **商品情報の編集**:
   - 既存の商品情報（名前と価格）を更新できます。

5. **データベース操作**:
   - SQLiteまたはPostgreSQLを使用してデータを永続化します。

## ディレクトリ構造

```
flask-product-management/
├── app/
│   ├── __init__.py          # Flaskアプリケーションとデータベースの初期化
│   ├── models.py            # データベースモデルの定義
│   ├── routes.py            # アプリケーションルートの定義
│   ├── templates/           # HTMLテンプレートフォルダ
│   │   ├── menu.html        # 管理メニュー画面
│   │   ├── view_products.html # 商品一覧画面
│   │   ├── edit_product.html # 商品編集画面
│   │   └── add_product.html  # 新規商品登録画面
├── .gitignore               # Git管理から除外するファイル
├── .env                     # 環境変数（データベース設定）
├── requirements.txt         # 必要なPythonライブラリ
├── README.md                # アプリケーションの説明
└── run.py                   # アプリケーションのエントリーポイント
```

## セットアップ方法

### 1. 仮想環境を作成する
以下のコマンドを実行して仮想環境を作成・有効化します。

```bash
python -m venv venv
source venv/bin/activate       # Windowsの場合: venv\Scripts\activate
```

### 2. 必要なパッケージをインストールする
以下のコマンドを実行して依存関係をインストールします。

```bash
pip install -r requirements.txt
```

### 3. 環境変数を設定する
プロジェクトのルートフォルダに`.env`ファイルを作成し、以下の内容を記載します。

```
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=your_database
```

### 4. データベースを初期化する
以下のコマンドを実行してデータベースを初期化します。

```bash
flask init-db
```

### 5. アプリケーションを起動する
以下のコマンドでアプリケーションを起動します。

```bash
python run.py
```

ブラウザで `http://127.0.0.1:5000/` にアクセスして動作を確認します。

## 使用技術

- **Flask**: Webアプリケーションフレームワーク
- **Flask-SQLAlchemy**: データベース操作のための拡張
- **Python-Dotenv**: 環境変数の管理
- **HTML**: フロントエンド


