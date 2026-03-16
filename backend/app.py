from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv
from werkzeug.security import check_password_hash

load_dotenv()

app = Flask(__name__, 
            template_folder='../frontend/templates', 
            static_folder='../frontend/static')

app.secret_key = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u_name = request.form.get('username')
        p_word = request.form.get('password')
        
        user = User.query.filter_by(username=u_name).first()
        
        # SİBER GÜVENLİK ANALİZİ (Terminalden izle)
        if user:
            print(f"[*] Kullanıcı bulundu: {u_name}")
            if check_password_hash(user.password, p_word):
                print("[+] Şifre doğrulandı! Giriş başarılı.")
                session['logged_in'] = True
                return redirect(url_for('admin'))
            else:
                print("[-] Şifre HATALI! Girdiğin şifreyi kontrol et.")
        else:
            print(f"[!] '{u_name}' isimli kullanıcı veritabanında yok!")
            
        return "Erişim Reddedildi: Kimlik doğrulama başarısız."
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        p_title = request.form.get('title')
        p_content = request.form.get('content')
        new_post = Post(title=p_title, content=p_content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('admin.html')

@app.route('/delete/<int:id>')
def delete_post(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)