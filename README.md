# 商品管理システム

このアプリケーションは、商品を管理するためのシンプルなシステムです。Python (Flask) を使用して構築されており、PostgreSQL をバックエンドデータベースとして使用します。

---

## **機能一覧**

- **商品一覧の表示**  
  登録されているすべての商品を一覧表示します。
- **新規商品の追加**  
  商品名と価格を入力して新しい商品を登録します。
- **商品の編集**  
  既存の商品情報（名前や価格）を更新します。
- **商品データの保存**  
  PostgreSQL データベースにデータを永続化します。

---

## **必要要件**

以下が事前にインストールされている必要があります：

- **Python 3.8+**
- **PostgreSQL 10+**
- **Git**（任意）

---

## **セットアップ手順**

### **1. リポジトリのクローンまたはダウンロード**
プロジェクトを取得します。

```bash
git clone https://github.com/your-repository-url.git
cd your-repository-name
```

---

### **2. 仮想環境を作成**
Python の仮想環境を作成して有効化します。

```bash
python3 -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

---

### **3. 必要なライブラリをインストール**

```bash
pip install -r requirements.txt
```

---

### **4. PostgreSQLデータベースのセットアップ**

1. PostgreSQLにログインします：

   ```bash
   sudo -u postgres psql
   ```

2. データベースとユーザーを作成：

   ```sql
   CREATE DATABASE product_db;
   CREATE USER product_user WITH PASSWORD 'password123';
   GRANT ALL PRIVILEGES ON DATABASE product_db TO product_user;
   ```

3. 必要なテーブルを作成：

   ```sql
   \c product_db
   CREATE TABLE products (
       id SERIAL PRIMARY KEY,
       name VARCHAR(120) UNIQUE NOT NULL,
       price FLOAT NOT NULL
   );
   ```

4. ダミーデータを追加（任意）：

   ```sql
   INSERT INTO products (name, price) VALUES
   ('りんご', 100),
   ('バナナ', 200),
   ('オレンジ', 150);
   ```

5. PostgreSQLからログアウト：

   ```sql
   \q
   ```

---

### **5. `.env` ファイルを作成**

プロジェクトフォルダに `.env` ファイルを作成し、以下を記載します：

```plaintext
DB_USERNAME=product_user
DB_PASSWORD=password123
DB_HOST=localhost
DB_NAME=product_db
SECRET_KEY=supersecretkey
```

---

### **6. アプリケーションを起動**

以下のコマンドでアプリケーションを起動します：

```bash
python run.py
```

---

## **使い方**

1. **ブラウザでアクセス**  
   以下のURLにアクセスします：

   ```
   http://127.0.0.1:5000/
   ```

2. **機能の説明**
   - **管理メニュー**: トップページで商品管理の各機能にアクセスできます。
   - **商品一覧**: 登録されている商品を表示します。
   - **新規商品登録**: 商品名と価格を入力して登録します。
   - **商品編集**: 商品名や価格を変更します。

---

## **よくある問題と解決方法**

1. **PostgreSQLに接続できない**
   - `.env` ファイルの内容が正しいか確認してください。
   - PostgreSQLが起動しているか確認します：
     ```bash
     sudo service postgresql status
     ```

2. **テーブルが見つからないエラー**
   - `products` テーブルが存在するか確認し、存在しない場合は再作成してください。

3. **依存ライブラリのエラー**
   - 必要なライブラリがインストールされているか確認：
     ```bash
     pip install -r requirements.txt
     ```

---

## **開発に関する情報**

- **Pythonバージョン**: 3.8+
- **フレームワーク**: Flask
- **データベース**: PostgreSQL

---

## **ライセンス**

このプロジェクトは [MIT ライセンス](https://opensource.org/licenses/MIT) のもとで公開されています。
