from flask import Flask, render_template

# フラスクインsタンスの作成
app = Flask(__name__)

# ルートデコレーターの作成
@app.route('/')
def index():
    first_name = "John"
    stuff = "This is bold Text"

    favorite_pizza = ["Pepparoni", "Cheese", "Mashroom", 41]
    return render_template('index.html',
    first_name=first_name,
    stuff=stuff,
    favorite_pizza=favorite_pizza)

# localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# カスタムエラーページ
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# インターナルサーバーエラーページ
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
