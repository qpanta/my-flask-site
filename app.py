import os
from flask import Flask, render_template, request, redirect, url_for
# Автоматично знаходимо папку, де лежить цей файл app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Жорстко вказуємо шлях до папки templates поруч
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route('/', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        user_login = request.form.get('username')
        user_password = request.form.get('password')
        
        print(f"Користувач {user_login} успішно ввів пароль!") 
        return redirect(url_for('main_site_page'))

    # Тепер Flask точно знає, де шукати цей файл
    return render_template('register.html')

@app.route('/home')
def main_site_page():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
